from django.shortcuts import render
from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name="about"),
    path('contactUs', views.contactUs, name="contactUs"),
    path('loginPage', views.handleLoginPage, name="Sign in"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('blog', views.blogHome, name="bloghome"),
    path('blog/<str:slug>', views.blogPost, name="blogPost"),
    path('post_event', views.event, name="event"),
    path('post_event/<str:slug>', views.eventsDetails, name="eventsDetails"),
    path('upcoming_event/<str:slug>', views.upcoming_event, name="eventsDetails_upcoming"),
    path('subscribe', views.subscribe, name="subscribe"),
]
