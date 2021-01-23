from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from contracts.forms import ContractForm

from contracts.models import Contract


@login_required
def index(request):
    contract_list = Contract.objects.all()

    page = request.GET.get("page", 1)

    paginator = Paginator(contract_list, 20)
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)

    context = {"collection": contracts}

    return render(request, "contracts/index.html", context)


@login_required
def new(request):
    """Create a new contract or etit an existing one."""
    if request.method != "POST":
        form = ContractForm(initial={"contract_number": "123"})
    else:
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.owner = request.user
            contract.save()
            return redirect(reverse("contracts:index"))

    context = {"form": form}
    return render(request, "contracts/new.html", context)


@login_required
def edit(request, contract_id):
    """Edit an existing contract."""
    contract = get_object_or_404(Contract, pk=contract_id)

    if request.method == "POST":
        form = ContractForm(instance=contract, data=request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            if not contract.owner:
                contract.owner = request.user
            contract.save()
            return redirect(reverse("contracts:index"))

    form = ContractForm(instance=contract)
    context = {"form": form, "contract": contract}

    return render(request, "contracts/edit.html", context)
