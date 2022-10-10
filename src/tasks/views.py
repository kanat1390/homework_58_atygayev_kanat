from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.base import TemplateView

from tasks.services import get_task_list, get_task_by_pk
from tasks.forms import TaskForm
from django.http import Http404


class TaskListView(TemplateView):

    template_name = 'tasks/task_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        task_list =get_task_list()
        context['task_list'] = task_list
        return context

class TaskDetailView(TemplateView):

    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_task_by_pk(kwargs.get('pk'))
        context['task'] = task
        return context


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {
            'form': form,
        }
        return render(request, 'tasks/task_create.html', context)
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        context = {
            'form':form,
        }
        return render(request, 'tasks/task_create.html', context)
        


class TaskUpdateView(View):
    
    def get(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs['pk'])
        form = TaskForm(instance=task)
        context = {
            'form': form,
        }
        return render(request, 'tasks/task_update.html', context)
    
    def post(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        else:
            context = {
                'form':form,
            }
            return render(request, 'tasks/task_update.html', context)

class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs['pk'])
        context = {
            'task':task,
        }
        return render(request, 'tasks/task_delete.html', context)
        
    def post(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs['pk'])
        task.delete()
        return redirect('task-list')



