from django.urls import path
from . import views

urlpatterns = [
    path('',views.greetingPage, name='greetingPage'),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('condition',views.condition,name='condition'),
    path('consultation',views.consultation, name='consultation'),
    path('lab',views.lab, name='lab'),
    path('pharmacy',views.pharmacy, name='pharmacy'),
    path('prescription',views.prescription, name='prescription'),
    path('accounts',views.accounts, name='accounts'), 
    path('logout',views.logout,name='logout')   
]
