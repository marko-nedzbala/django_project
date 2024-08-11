from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import TaskList

# import the form
from todo.forms import TaskForm
# Create your views here.
@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            # print('Request', request.user)
            form.save()

            # form.instance.owner = request.user
            # form.save()

            # own = form.save(commit=False)
            # own.user_creator = request.user
            # own.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todolist')
    else:
        # an object of our model with all the items
        all_tasks = TaskList.objects.filter(owner=request.user)
        # separate it every 2 items
        paginator = Paginator(all_tasks, 2)
        # for &pg=page_number in the URL
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        # context = {
        #     'welcome_text': 'Welcome to the Todo List'
        # }
        return render(request, 'todolist.html', context={'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else: 
        messages.error(request, ('Accesss Restricted.'))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ('Task Edited'))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', context={'task_obj': task_obj})

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else: 
        messages.error(request, ('Accesss Restricted.'))
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def contact(request):
    context = {
        'contact_text': 'Welcome to the Contact List'
    }
    return render(request, 'contact.html', context=context)

def about(request):
    context = {
        'about_text': 'Welcome to the About List'
    }
    return render(request, 'about.html', context=context)

def index(request):
    context = {
        'index_text': 'Welcome to the Index'
    }
    return render(request, 'index.html', context=context)