from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Deal
from .forms import DealForm


@login_required
def deal_list(request):

    search = request.GET.get('search')

    deals = Deal.objects.filter(
        company=request.user.company
    ).order_by('-id')

    if search:
        deals = deals.filter(
            title__icontains=search
        )

    paginator = Paginator(deals, 10)
    page_number = request.GET.get('page')
    deals = paginator.get_page(page_number)

    return render(
        request,
        'deals/list.html',
        {
            'deals': deals
        }
    )


@login_required
def deal_create(request):

    form = DealForm()

    if request.method == "POST":

        form = DealForm(request.POST)

        if form.is_valid():

            deal = form.save(commit=False)

            deal.company = request.user.company

            deal.save()

            return redirect('deal_list')

    return render(
        request,
        'deals/add.html',
        {
            'form': form
        }
    )


@login_required
def deal_update(request, pk):

    deal = get_object_or_404(
        Deal,
        pk=pk,
        company=request.user.company
    )

    form = DealForm(instance=deal)

    if request.method == "POST":

        form = DealForm(
            request.POST,
            instance=deal
        )

        if form.is_valid():

            form.save()

            return redirect('deal_list')

    return render(
        request,
        'deals/add.html',
        {
            'form': form
        }
    )


@login_required
def deal_delete(request, pk):

    deal = get_object_or_404(
        Deal,
        pk=pk,
        company=request.user.company
    )

    deal.delete()

    return redirect('deal_list')


@login_required
def deal_detail(request, pk):

    deal = get_object_or_404(
        Deal,
        pk=pk,
        company=request.user.company
    )

    return render(
        request,
        'deals/detail.html',
        {
            'deal': deal
        }
    )