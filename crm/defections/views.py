from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Defection, Photo
from .forms import DefectionForm
from accounts.models import Account
from shipments.models import ShipmentOffering


def index(request, account_extid):
    accounts = Account.objects.filter(extid=account_extid.upper())
    if accounts.exists():
        account = accounts[0]
        defections = Defection.objects.filter(account=account)
        context = {'defections': defections, 'account': account}
    else:
        context = {'account': 'Контрагент не идентифицирован'}

    return render(request, 'defections/index.html', context)


def defection(request, account_extid, defection_id):
    '''Выводит акт обнаружения брака для просмотра'''
    defection = Defection.objects.get(id=defection_id)
    account = Account.objects.get(extid=account_extid.upper())
    context = {'defection': defection, 'account': account}
    return render(request, 'defections/defection.html', context)


def new_defection(request, account_extid):
    account = Account.objects.get(extid=account_extid.upper())
    if request.method != 'POST':
        form = DefectionForm(account)
    else:
        form = DefectionForm(account, request.POST, request.FILES)
        if form.is_valid():
            new_defection = form.save(commit=False)
            new_defection.account = account
            new_defection.save()
            notify(new_defection)

            files = request.FILES.getlist('damage_photo')
            for f in files:
                photo = Photo()
                photo.defection = new_defection
                photo.title = 'Фото повреждения'
                photo.file = f
                photo.save()

            return HttpResponseRedirect(reverse('defections:index', args=[account_extid]))

    context = {'form': form, 'extid': account_extid, 'account': account}
    return render(request, 'defections/new_defection.html', context)


def load_offerings(request):
    shipment_id = request.GET.get('shipment')
    shipment_offerings = ShipmentOffering.objects.filter(shipment_id=shipment_id)
    offerings = []
    for row in shipment_offerings:
        offerings.append(row.offering)

    return render(request, 'defections/offering_list.html', {'offerings': offerings})


def notify(defection):
    subject = 'Новый акт обнаружения брака!'
    message = f'''
        Контрагент: {defection.account}\n
        Документ отгрузки: {defection.shipment}\n
        Оборудование: {defection.offering}\n
        Серийный номер: {defection.serial_number}'''

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        'n.bayborodin@skatpower.ru',
        'k.davydov@skatpower.ru',
    ]

    send_mail(subject, message, email_from, recipient_list)
