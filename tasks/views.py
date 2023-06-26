from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
# Create your views here.


class TaskListView(ListView):
    model = Task    # 'task_list'
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task    # 'task_list'
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'



class TaskDeleteView(DeleteView):
    model = Task    # 'task_list'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('index')

    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)

class TaskUpdateView(UpdateView):
    model = Task    # 'task_list'
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('index')
    fields = ['title', 'descript','task_image','deadline']


class TaskCreateView(CreateView):
    model = Task
    fields = ['title','descript','task_image','deadline']
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



