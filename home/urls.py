from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('students/', views.students, name='students'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('404/', views.snake, name='404')
]