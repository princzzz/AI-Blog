from django.shortcuts import redirect, render, HttpResponse
from .models import Blog
from home.models import  Contact, PreEvent, PostEvent, Email
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
import datetime
from django.db import IntegrityError
def home(request):
    events = PreEvent.objects.all()
    allPosts= Blog.objects.all()
    context={'allPosts': allPosts,'events':events}
    return render(request,"home/index.html",context)
def about(request):
    return render(request,"home/about.html")

def handleLoginPage(request):
    return render(request,'home/loginPage.html')

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            params={"message":"successfully logged in","color":"text-green-600"}
            return render(request,"home/loginPage.html",params)
        else:
            params={"message":"Invalid credentials! Please try again","color":"text-red-600"}
            return render(request,'home/loginPage.html',params)

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    params={"message":"successfully logged out","color":"text-green-600"}
    return render(request,"home/loginPage.html",params)

def contactUs(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['message']
        temp = Contact(name=name,email=email,content=content,timeStamp=datetime.datetime.now())
        temp.save()
    return render(request,'home/contactUs.html')


def blogHome(request):
    allPosts= Blog.objects.filter(is_approved=True)
    context={'allPosts': allPosts}
    return render(request,"blog/index.html",context)


def blogPost(request, slug):
    post=Blog.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    context={'post':post}
    return render(request,"blog/posts.html",context)

#This 2 are the post event and details function
def event(request):
    events = PostEvent.objects.all()
    params = {'events':events}
    return render(request,'event/post_event.html',params)

def eventsDetails(request,slug):
    a=PostEvent.objects.get(slug=slug)
    params={"a":a}
    return render(request,'event/post_event_details.html',params)

#This is the upcoming event details function

def upcoming_event(request,slug):
    a=PreEvent.objects.get(slug=slug)
    params={"a":a}
    return render(request,'event/pre_event_details.html',params)


def subscribe(request):
    if request.method=="POST":
        email=request.POST['email']
        temp = Email(address=email)
        try:
            temp.save()
        except IntegrityError as e:
            pass
    return redirect('home')