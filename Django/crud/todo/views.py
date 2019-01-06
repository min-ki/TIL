from django.shortcuts import render, redirect
from todo.models import Todo
from .forms import TodoForm


def todo_list(request):

    todos = Todo.objects.all()  # todo 리스트
    context = {}
    context['todos'] = todos

    return render(request, 'todo/todo_list.html', context=context)


def todo_create(request):

    if request.method == "POST":
        todoForm = TodoForm(request.POST)
        if todoForm.is_valid():
            todo = todoForm.save(commit=False)
            print(request.POST)
            todo.save()
            return redirect('todo:todo_list')
    else:
        todoForm = TodoForm()
    return render(request, 'todo/todo_create.html', {
        'todoForm': todoForm
    })
