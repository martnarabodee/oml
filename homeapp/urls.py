from django.urls import path
from . import views

app_name = "homeapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('complain_form', views.complain_form, name="complain_form"),
    #path('complain/success', views.complain_success, name="complain_success"),
    #path('profile', views.profile, name='profile'),
    #path('term', views.term, name='term'),
    #path('signin_success', views.signin_success, name='signin_success'),
    path('error', views.error, name='error'),
]