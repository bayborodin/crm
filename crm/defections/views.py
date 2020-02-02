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

            print('DBG!!!')
            print(request.FILES)
            files = request.FILES.getlist('damage_photo')
            for f in files:
                print(f)
                photo = Photo()
                photo.defection = new_defection
                photo.title = 'Фото повреждения'
                photo.file = f
                photo.save()

            return HttpResponseRedirect(reverse('defections:index', args=[account_extid]))

    context = {'form': form, 'extid': account_extid}
    return render(request, 'defections/new_defection.html', context)


def load_offerings(request):
    shipment_id = request.GET.get('shipment')
    shipment_offerings = ShipmentOffering.objects.filter(shipment_id=shipment_id)
    offerings = []
    for row in shipment_offerings:
        offerings.append(row.offering)

    return render(request, 'defections/offering_list.html', {'offerings': offerings})
