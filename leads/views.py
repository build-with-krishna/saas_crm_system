from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Lead
from .forms import LeadForm


@login_required
def lead_list(request):

    search = request.GET.get('search')

    leads = Lead.objects.filter(
        company=request.user.company
    ).order_by('-id')

    if search:
        leads = leads.filter(
            name__icontains=search
        )

    paginator = Paginator(leads, 10)
    page_number = request.GET.get('page')
    leads = paginator.get_page(page_number)

    return render(
        request,
        'leads/list.html',
        {
            'leads': leads
        }
    )


@login_required
def lead_create(request):

    form = LeadForm()

    if request.method == "POST":

        form = LeadForm(request.POST)

        if form.is_valid():

            lead = form.save(commit=False)
            lead.company = request.user.company
            lead.save()

            return redirect('lead_list')

    return render(
        request,
        'leads/add.html',
        {
            'form': form
        }
    )


@login_required
def lead_update(request, pk):

    lead = get_object_or_404(
        Lead,
        pk=pk,
        company=request.user.company
    )

    form = LeadForm(instance=lead)

    if request.method == 'POST':

        form = LeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            return redirect('lead_list')

    return render(
        request,
        'leads/add.html',
        {
            'form': form
        }
    )


@login_required
def lead_delete(request, pk):

    lead = get_object_or_404(
        Lead,
        pk=pk,
        company=request.user.company
    )

    lead.delete()

    return redirect('lead_list')