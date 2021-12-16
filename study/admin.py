from django.contrib import admin
from . import models

class CourseInfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.CourseInfo._meta.fields]

admin.site.register(models.CourseInfo)
admin.site.register(models.CourseVideo)
admin.site.register(models.CourseMaterial)
admin.site.register(models.RegisterCourse)
admin.site.register(models.ProblemInfoDeep)

