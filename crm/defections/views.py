from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Defection
from .forms import DefectionForm
from accounts.models import Account


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
        form = DefectionForm()
    else:
        form = DefectionForm(request.POST)
        if form.is_valid():
            new_defection = form.save(commit=False)
            new_defection.account = account
            new_defection.save()
            return HttpResponseRedirect(reverse('defections:index', args=[account_extid]))

    context = {'form': form, 'extid': account_extid}
    return render(request, 'defections/new_defection.html', context)
