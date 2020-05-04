from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index , name='index'),
    path('add_todo/', views.add_todo),  
    path('delete_todo/<int:todo_id>/', views.delete_todo),
    path('modify_todo/<int:todo_id>/', views.modify_todo),
]