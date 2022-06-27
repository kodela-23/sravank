# from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landing_page', views.landing_page, name='landing_page'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('add_task', views.add_task, name='add_task'),
    path('delete/<int:id>', views.delete, name='delete'),
]