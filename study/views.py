from django.shortcuts import render

# Create your views here.
def course_home(request):
    return render(request, 'study/course_home.html')

def course_select_class(request):
    return render(request, 'study/course_select_class.html')

def course_select_custom(request):
    return render(request, 'study/course_select_custom.html')

def course_instruction(request):
    return render(request, 'study/course_instruction.html')

def course_warn(request):
    return render(request, 'study/course_warn.html')

def course_continue(request):
    return render(request, 'study/course_continue.html')

def course_sheet(request):
    return render(request, 'study/course_sheet.html')

def course_study(request):
    return render(request, 'study/course_study.html')

def course_summary(request):
    return render(request, 'study/course_summary.html')

def course_certificate(request):
    return render(request, 'study/course_certificate.html')

def problem_select(request):
    return render(request, 'study/problem_select.html')

def problem_do(request):
    return render(request, 'study/problem_do.html')
