from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AccountForm
from .models import Account


@login_required
def index(request):
    """The main page for the accounts application"""
    account_list = Account.objects.order_by("name")
    page = request.GET.get("page", 1)

    paginator = Paginator(account_list, 20)
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    except EmptyPage:
        accounts = paginator.page(paginator.num_pages)

    context = {"collection": accounts}

    return render(request, "accounts/index.html", context)


@login_required
def new(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect("/accounts")

    form = AccountForm()
    return render(request, "accounts/edit.html", {"form": form})


@login_required
def edit(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            if not account.owner:
                account.owner = request.user
            account.save()
            return redirect("/accounts")

    form = AccountForm(instance=account)
    context = {"form": form, "account_name": account.name}

    return render(request, "accounts/edit.html", context)


@login_required
def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    context = {"account": account}

    return render(request, "accounts/detail.html", context)
