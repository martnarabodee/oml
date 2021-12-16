from django.urls import path
from . import views

app_name = "study"

urlpatterns = [
    path('course/home', views.course_home, name='course_home'),
    path('course/select_class', views.course_select_class, name='course_select_class'),
    path('course/select_custom', views.course_select_custom, name='course_select_custom'),
    path('course/instruction', views.course_instruction, name='course_instruction'),
    path('course/warn', views.course_warn, name='course_warn'),
    path('course/continue', views.course_home, name='course_continue'),
    path('course/sheet', views.course_sheet, name='course_sheet'),
    path('course/study', views.course_study, name='course_study'),
    path('course/summary', views.course_summary, name='course_summary'),
    path('course/certificate', views.course_certificate, name='course_certificate'),
    path('problem/select', views.problem_select, name='problem_select'),
    path('problem/do', views.problem_do, name='problem_do'),
]