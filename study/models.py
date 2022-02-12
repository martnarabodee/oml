from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, URLField

# Create your models here.
class CourseInfo(models.Model):
    course_id  = models.PositiveIntegerField(primary_key=True, default=1)
    course_name = models.CharField(max_length=100)
    course_description = models.CharField
    is_use = models.BooleanField(default=True)

    def __str__(self):
        return self.caption

'''
class CourseVideo (models.Model):
    cv_id = models.PositiveIntegerField #course video id
    cv_lecturer = models.CharField 
    cv_video = URLField
    is_use = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.cv_id


class CourseMaterial (models.Model):
    course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    cv_id = models.ForeignKey(CourseVideo, on_delete=models.CASCADE) 
    cm_worksheet = models.FileField     #store course's worksheet
    is_use = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.course_id


class RegisterCourse (models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    RegisterCourseTime = models.DateTimeField


# Problem Classes
class ProblemInfoDeep (models.Model):
    pb_id = models.IntegerField(primary_key=True)
    pb_material = models.JSONField
    pb_hard = models.SmallIntegerField
    pb_error = models.JSONField
    pb_size = models.SmallIntegerField
    pb_source = models.CharField

""""
class ProblemKeyInteger (models.Model):
    pb_id = models.ManyToManyField(ProblemInfoDeep, primary_key=True)
    pb_key = models.IntegerField

class ProblemKeyChar (models.Model):
    pb_id = models.ManyToManyField(ProblemInfoDeep, primary_key=True)
    pb_key = models.CharField

class ProblemKeyPicture (models.Model):
    pb_id = models.ManyToManyField(ProblemInfoDeep, primary_key=True)
    pb_id = models.ImageField

class ProblemInfoShow (models.Model):
    pb_id = models.ManyToManyField(ProblemInfoDeep, primary_key=True)
    pb_key = models.ForeignKey(ProblemInfoDeep, on_delete=models.CASCADE)
    pb_image = models.ImageField
    pb_status = models.SmallIntegerField
    pb_donescore = models.SmallIntegerField
    pb_type = models.SmallIntegerField
"""'''

class VideoDemo(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption