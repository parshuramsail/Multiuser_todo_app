from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        form = TodoForm()
        todos = Todo.objects.filter(user=request.user).order_by('priority')
        return render(request, 'todo/index.html', {'form': form, 'todos': todos})
    else:
        return redirect('login')


# def login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     loginUser(request, user)
#                     return redirect('home')
#         else:
#             form = AuthenticationForm()
#         return render(request, 'todo/login.html', {'form': form})
#     else:
#         return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})


@ login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, 'index.html', {'form': form})


def delete_todo(request, id):
    Todo.objects.get(pk=id).delete()
    return redirect('home')


def change_todo(request, id, status):
    todo = Todo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')


# def signout(request):
#     logout(request)
#     return redirect('login')
