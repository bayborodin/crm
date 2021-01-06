from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Contract


def index(request):
    contract_list = Contract.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(contract_list, 20)
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)

    context = {'collection': contracts}

    return render(request, 'contracts/index.html', context)
