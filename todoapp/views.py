from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import tasks

# Create your views here.

def landing_page(request):
    return render (request, 'login_registration.html')


def index(request):
    if request.user.username == '':
        return redirect('/landing_page')
    else:
        task = tasks.objects.filter(username = request.user.username)
        return render (request, 'index.html', {'task': task})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login_registration.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists == False:
                messages.info(request, 'Username Taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
        return redirect('/')

    else:
        return render(request, 'login_registration.html')


def add_task(request):
    if request.method == 'POST':
        task = tasks()

        # task.username
        task.title = request.POST['title']
        task.description = request.POST['description']
        try:
            task.important = request.POST['important']
        except:
            pass
        task.username = request.user.username
        task.save()
        return redirect('/')

    else:
        return render(request, 'login_registration.html')


def delete(request, id):
    tasks.objects.get(id=id).delete()
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/landing_page')