from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Customer
from .forms import CustomerForm


@login_required
def customer_list(request):

    search = request.GET.get('search')

    customers = Customer.objects.filter(
        company=request.user.company
    ).order_by('-id')

    if search:
        customers = customers.filter(
            name__icontains=search
        )

    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)

    return render(
        request,
        'customers/list.html',
        {
            'customers': customers
        }
    )


@login_required
def customer_create(request):

    form = CustomerForm()

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():

            customer = form.save(commit=False)

            customer.company = request.user.company

            customer.save()

            return redirect('customer_list')

    return render(
        request,
        'customers/add.html',
        {
            'form': form
        }
    )


@login_required
def customer_update(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk,
        company=request.user.company
    )

    form = CustomerForm(instance=customer)

    if request.method == 'POST':

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():
            form.save()
            return redirect('customer_list')

    return render(
        request,
        'customers/add.html',
        {
            'form': form
        }
    )


@login_required
def customer_delete(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk,
        company=request.user.company
    )

    customer.delete()

    return redirect('customer_list')


@login_required
def customer_detail(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk,
        company=request.user.company
    )

    return render(
        request,
        'customers/detail.html',
        {
            'customer': customer
        }
    )