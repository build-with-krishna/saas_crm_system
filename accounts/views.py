from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CompanySignupForm
from .models import User
from companies.models import Company

from django.contrib.auth import authenticate, login, logout
from .forms import CompanySignupForm, LoginForm
from django.contrib.auth.decorators import login_required


from datetime import date, timedelta
from subscriptions.models import Plan, Subscription


def company_signup(request):

    if request.method == "POST":
        form = CompanySignupForm(request.POST)

        if form.is_valid():

            # 1. Create Company
            company = Company.objects.create(
                name=form.cleaned_data['company_name'],
                email=form.cleaned_data['email']
            )

            # 2. Create Admin User
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password'],
                role='admin',
                company=company,
                is_staff=True
            )

            trial_plan = Plan.objects.get(name='Free Trial')

            Subscription.objects.create(

                company=company,

                plan=trial_plan,

                start_date=date.today(),

                end_date=date.today() + timedelta(
                    days=trial_plan.duration_days
                ),

                status='active'

            )

            # 3. Auto login
            login(request, user)

            return redirect('/dashboard/')

    else:
        form = CompanySignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):

    if request.user.is_authenticated:
        return redirect('/dashboard/')

    form = LoginForm()

    if request.method == 'POST':

        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/dashboard/')

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')