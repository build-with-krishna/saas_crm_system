from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import FollowUp
from .forms import FollowUpForm


@login_required
def followup_list(request):

    followups = FollowUp.objects.filter(
        company=request.user.company
    ).order_by('-id')

    return render(
        request,
        'followups/list.html',
        {
            'followups': followups
        }
    )


@login_required
def followup_create(request):

    form = FollowUpForm()

    if request.method == "POST":

        form = FollowUpForm(request.POST)

        if form.is_valid():

            obj = form.save(commit=False)

            obj.company = request.user.company

            obj.save()

            return redirect('followup_list')

    return render(
        request,
        'followups/add.html',
        {
            'form': form
        }
    )