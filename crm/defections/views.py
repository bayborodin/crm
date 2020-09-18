import tempfile

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from weasyprint import HTML

from accounts.models import Account
from .forms import DefectionForm
from .models import Defection, Photo
from shipments.models import ShipmentOffering


def index(request, account_extid):
    """List the account's defections records."""
    accounts = Account.objects.filter(extid=account_extid.upper())
    if accounts.exists():
        account = accounts[0]
        defections = Defection.objects.filter(account=account)
        context = {'defections': defections, 'account': account}
    else:
        context = {'account': 'Контрагент не идентифицирован'}

    return render(request, 'defections/index.html', context)


def defection(request, account_extid, defection_id):
    """Выводит акт обнаружения брака для просмотра."""
    defection = Defection.objects.get(id=defection_id)
    account = Account.objects.get(extid=account_extid.upper())
    context = {'defection': defection, 'account': account}
    return render(request, 'defections/defection.html', context)


def pdf(request, account_extid, defection_id):
    """Generate a PDF for a defection report."""
    # Model data
    defection = Defection.objects.get(id=defection_id)

    # Render
    buyer_legal_entity = defection.shipment.buyer
    seller_name = defection.shipment.seller.name
    seller_name = seller_name.replace(
        'Общество с ограниченной ответственностью',
        'Общества с ограниченной ответственностью',
    )
    seller_name = seller_name.replace(
        'Индивидуальный предприниматель',
        'Индивидуального предпринимателя',
    )
    context = {
        'defection': defection,
        'buyer_legal_entity': buyer_legal_entity,
        'seler_name': seller_name,
    }
    html_string = render_to_string('defections/pdf.html', context)
    html = HTML(string=html_string)
    pdf_document = html.write_pdf()

    # Create HTTP response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=defection.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(pdf_document)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def new_defection(request, account_extid):
    """Create a new defection from a form data."""
    account = Account.objects.get(extid=account_extid.upper())
    if request.method != 'POST':
        form = DefectionForm(account)
    else:
        form = DefectionForm(account, request.POST, request.FILES)
        if form.is_valid():
            new_defection = form.save(commit=False)
            new_defection.account = account
            new_defection.save()

            files = request.FILES.getlist('damage_photo')
            for damage_photo in files:
                photo = Photo()
                photo.defection = new_defection
                photo.title = 'Фото повреждения'
                photo.file = damage_photo
                photo.save()

            files = request.FILES.getlist('package_photo_outside')
            for outside_photo in files:
                photo = Photo()
                photo.defection = new_defection
                photo.title = 'Фото повреждения упаковки (снаружи)'
                photo.file = outside_photo
                photo.save()

            files = request.FILES.getlist('package_photo_inside')
            for inside_photo in files:
                photo = Photo()
                photo.defection = new_defection
                photo.title = 'Фото повреждения упаковки (изнутри)'
                photo.file = inside_photo
                photo.save()

            notify(request, new_defection)

            return HttpResponseRedirect(
                reverse('defections:index', args=[account_extid])
            )

    context = {'form': form, 'extid': account_extid, 'account': account}
    return render(request, 'defections/new_defection.html', context)


def load_offerings(request):
    """Load offerings for a shipment with a given id."""
    shipment_id = request.GET.get('shipment')
    shipment_offerings = ShipmentOffering.objects.filter(
        shipment_id=shipment_id,
    )
    offerings = []
    for row in shipment_offerings:
        offerings.append(row.offering)

    return render(
        request, 'defections/offering_list.html', {'offerings': offerings},
    )


def notify(request, defection):
    """Send an email nitification about a new defection."""
    subject = 'Новый акт обнаружения брака!'

    photo_list = '\nПриложенные файлы:\n'
    for photo in defection.photos.all():
        url = request.build_absolute_uri(photo.file.url)
        photo_list += f'{url}\n'

    message = f'''
        Контрагент: {defection.account}\n
        Документ отгрузки: {defection.shipment}\n
        Оборудование: {defection.offering}\n
        Серийный номер: {defection.serial_number}\n'''
    message += photo_list

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        'n.bayborodin@skatpower.ru',
    ]
    if defection.account.owner.email:
        recipient_list.append(defection.account.owner.email)

    send_mail(subject, message, email_from, recipient_list)
