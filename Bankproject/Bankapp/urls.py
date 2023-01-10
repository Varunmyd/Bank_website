from django.urls import path

from Bankapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('fillform', views.fillform, name='fillform'),
    path('logout', views.logout, name='logout'),
]
