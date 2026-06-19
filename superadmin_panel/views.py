from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from companies.models import Company
from accounts.models import User
from subscriptions.models import Subscription, Plan

from django.db.models import Sum
from datetime import date, timedelta

@staff_member_required
def admin_dashboard(request):

    total_plans = Plan.objects.count()

    monthly_revenue = Subscription.objects.filter(
        status='active'
    ).aggregate(
        total=Sum('plan__price')
    )['total'] or 0

    expired_subscriptions = Subscription.objects.filter(
        status='expired'
    ).count()

    total_companies = Company.objects.count()

    active_companies = Company.objects.filter(
        is_active=True
    ).count()

    total_users = User.objects.count()

    active_subscriptions = Subscription.objects.filter(
        status='active'
    ).count()

    context = {

        'total_companies': total_companies,

        'active_companies': active_companies,

        'total_users': total_users,

        'active_subscriptions': active_subscriptions,

        'total_plans': total_plans,

        'monthly_revenue': monthly_revenue,

        'expired_subscriptions': expired_subscriptions

    }

    return render(
        request,
        'superadmin/dashboard.html',
        context
    )


@staff_member_required
def company_list(request):

    companies = Company.objects.all().order_by('-id')

    return render(
        request,
        'superadmin/company_list.html',
        {
            'companies': companies
        }
    )


@staff_member_required
def company_suspend(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk
    )

    company.is_active = False

    company.save()

    return redirect('company_list')


@staff_member_required
def company_activate(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk
    )

    company.is_active = True

    company.save()

    return redirect('company_list')




@staff_member_required
def subscription_list(request):

    subscriptions = Subscription.objects.select_related(
        'company',
        'plan'
    ).order_by('-id')

    return render(
        request,
        'superadmin/subscription_list.html',
        {
            'subscriptions': subscriptions
        }
    )


@staff_member_required
def assign_plan(request, company_id):

    company = get_object_or_404(
        Company,
        pk=company_id
    )

    plans = Plan.objects.filter(
        is_active=True
    )

    if request.method == "POST":

        plan_id = request.POST.get('plan')

        plan = Plan.objects.get(
            id=plan_id
        )

        subscription, created = Subscription.objects.get_or_create(
            company=company,
            defaults={
                'plan': plan,
                'start_date': date.today(),
                'end_date': date.today()+timedelta(days=plan.duration_days),
                'status': 'active'
            }
        )

        if not created:

            subscription.plan = plan

            subscription.start_date = date.today()

            subscription.end_date = (
                date.today() +
                timedelta(days=plan.duration_days)
            )

            subscription.status = 'active'

            subscription.save()

        return redirect(
            'subscription_list'
        )

    return render(
        request,
        'superadmin/assign_plan.html',
        {
            'company': company,
            'plans': plans
        }
    )