from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    #print()
    #message="id:%s, uasername:%s firstname:%s, lastname:%s"%(request.user.pk, request.user.username, request.user.first_name, request.user.last_name)
    #now = datetime.datetime.now()
    return render(request, 'homeapp/home.html')

def about(request):
    return render(request, 'homeapp/about.html')

def contact(request):
    return render(request, 'homeapp/contact.html')

def complain_form(request):
    return render(request, 'homeapp/complain_form.html')

def complain_success(request):
    return render(request, 'homeapp/complain_success.html')

#from account
def profile(request):
    return render(request, 'homeapp/profile.html')

def term(request):
    return render(request, 'homeapp/term.html')

def register_student(request):
    return render(request, 'homeapp/register_student.html')

def register_teacher(request):
    return render(request, 'homeapp/register_teacher.html')

def register_success(request):
    return render(request, 'homeapp/register_success.html')

def signin_form(request):
    return render(request, 'homeapp/signin_form.html')

def signin_success(request):
    return render(request, 'homeapp/signin_success.html')
