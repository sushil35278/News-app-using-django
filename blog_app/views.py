from email.mime import image
from urllib import request
from django.shortcuts import render, redirect
from blog_app.models import News
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# @login_required
def home(request):
    news = News.objects.all()
    return render(request,'blog_app/home.html', context={'news':news})

# @login_required
def add_news(request):
    if request.method == 'GET':
        return render(request, 'blog_app/add-news.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        image = request.POST['image']
        News.objects.create(title=title, content=content, user_id = request.user.id)

        return redirect('home')

def edit_news(request, id):
    news =News.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'blog_app/edit-news.html', {'news':news})

    else:
        news.title = request.POST['title']
        news.content = request.POST['content']
        news.save()
        return redirect('home')

def delete_news(request, id):
    news = News.objects.get(id=id)
    news.delete()
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'user_app/signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('signin')

        

def register(request):
    if request.method == 'GET':
        return render(request, 'user_app/register.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)

        return redirect('signin')   


def signout(request):
    logout(request)

    return redirect('signin')