from django.shortcuts import render

from .models import Defection


def index(request, account_extid):
    defections = Defection.objects.filter(account__extid=account_extid)
    context = {'defections': defections}
    return render(request, 'defections/index.html', context)
