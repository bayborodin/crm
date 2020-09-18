from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Lead


def index(request):
    """Show list of all leads"""
    all_leads = Lead.objects.order_by('created')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_leads, 20)
    try:
        leads = paginator.page(page)
    except PageNotAnInteger:
        leads = paginator.page(1)
    except EmptyPage:
        leads = paginator.page(paginator.num_pages)

    context = {'collection': leads}

    return render(request, 'leads/index.html', context)
