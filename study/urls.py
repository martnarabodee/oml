from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "study"

urlpatterns = [
    path('course/home', views.course_home, name='course_home'),
    #path('course/select_class', views.course_select_class, name='course_select_class'),
    #path('course/select_custom', views.course_select_custom, name='course_select_custom'),
    path('course/instruction', views.course_instruction, name='course_instruction'),
    #path('course/warn', views.course_warn, name='course_warn'),
    #path('course/continue', views.course_home, name='course_continue'),
    #path('course/sheet', views.course_sheet, name='course_sheet'),
    path('course/study', views.course_study, name='course_study'),
    path('course/summary', views.course_summary, name='course_summary'),
    #path('course/certificate', views.course_certificate, name='course_certificate'),
    #path('problem/select', views.problem_select, name='problem_select'),
    #path('problem/do', views.problem_do, name='problem_do'),
    path('problem/demo/pre/instruction', views.problem_demo_pre1, name='problem_demo_pre1'),
    path('problem/demo/pre/choice', views.problem_demo_pre2, name='problem_demo_pre2'),
    path('problem/demo/pre/fillin', views.problem_demo_pre3, name='problem_demo_pre3'),
    path('problem/demo/post/instruction', views.problem_demo_post1, name='problem_demo_post1'),
    path('problem/demo/post/choice', views.problem_demo_post2, name='problem_demo_post2'),
    path('problem/demo/post/fillin', views.problem_demo_post3, name='problem_demo_post3'),
    path('download/<str:oml_sheet>', views.download_file, name='download_file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)