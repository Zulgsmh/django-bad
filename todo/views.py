from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#------------------------------ View To do app here.--------------------------------------------------------

def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/index.html', { 'todo_items':todo_items })

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    task_created = Todo.objects.create(added_date=current_date,text=content)
    #print(task_created)
    #print(task_created.id)
    #print(Todo.objects.all().count())
    return HttpResponseRedirect("/todo")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect("/todo")


@csrf_exempt
def modify_todo(request):
    pass