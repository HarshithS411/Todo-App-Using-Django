from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        if 'title' in request.POST:
            new_task = request.POST.get('title')
            Task.objects.create(title = new_task)
        elif 'delete' in request.POST:
            task_id = request.POST.get('delete')
            Task.objects.get(id = task_id).delete()
        return redirect('index')

    return render(request, 'index.html',{'tasks':tasks})