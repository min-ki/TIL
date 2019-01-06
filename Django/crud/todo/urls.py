from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create')
]
