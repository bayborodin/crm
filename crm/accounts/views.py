from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Account


def index(request):
    """The main page for the accounts application"""
    account_list = Account.objects.order_by('name')
    page = request.GET.get('page', 1)

    paginator = Paginator(account_list, 20)
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    except EmptyPage:
        accounts = paginator.page(paginator.num_pages)

    context = {'collection': accounts}

    return render(request, 'accounts/index.html', context)
