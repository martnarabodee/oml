from django.shortcuts import render
from .models import VideoDemo
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

# Create your views here.
def course_home(request):
    return render(request, 'study/course_home.html')

def course_select_class(request):
    return render(request, 'study/course_select_class.html')

def course_select_custom(request):
    return render(request, 'study/course_select_custom.html')

def course_instruction(request):
    return render(request, 'study/course_instruction.html')

# Define function to download pdf file using template
def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/study/static/study/sheet/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(pdf)
        response['Content-Type'] = 'application/pdf'
        response['Content-disposition'] = 'attachment ; filename = {}'.format(oml_sheet)
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'study/course_instruction.html')


def course_warn(request):
    return render(request, 'study/course_warn.html')

def course_continue(request):
    return render(request, 'study/course_continue.html')

def course_sheet(request):
    return render(request, 'study/course_sheet.html')

def course_study(request):
    video = VideoDemo.objects.all()
    return render(request,"study/course_study.html",{"video":video})

def course_summary(request):
    return render(request, 'study/course_summary.html')

def course_certificate(request):
    return render(request, 'study/course_certificate.html')

def problem_select(request):
    return render(request, 'study/problem_select.html')

def problem_do(request):
    return render(request, 'study/problem_do.html')

def problem_demo_pre1(request):
    return render(request, 'study/problem_demo_pre1.html')

def problem_demo_pre2(request):
    return render(request, 'study/problem_demo_pre2.html')

def problem_demo_pre3(request):
    return render(request, 'study/problem_demo_pre3.html')

def problem_demo_post1(request):
    return render(request, 'study/problem_demo_post1.html')

def problem_demo_post2(request):
    return render(request, 'study/problem_demo_post2.html')

def problem_demo_post3(request):
    return render(request, 'study/problem_demo_post3.html')