from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):

    search = request.GET.get('search')

    tasks = Task.objects.filter(
        company=request.user.company
    ).order_by('-id')

    if search:
        tasks = tasks.filter(
            title__icontains=search
        )

    paginator = Paginator(tasks, 10)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(
        request,
        'tasks/list.html',
        {
            'tasks': tasks
        }
    )


@login_required
def task_create(request):

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)
            task.company = request.user.company
            task.save()

            return redirect('task_list')

    return render(
        request,
        'tasks/add.html',
        {
            'form': form
        }
    )


@login_required
def task_update(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        company=request.user.company
    )

    form = TaskForm(instance=task)

    if request.method == "POST":

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            return redirect('task_list')

    return render(
        request,
        'tasks/add.html',
        {
            'form': form
        }
    )


@login_required
def task_delete(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
        company=request.user.company
    )

    task.delete()

    return redirect('task_list')