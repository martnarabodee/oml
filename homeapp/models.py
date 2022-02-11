from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.\
'''
class UserOptimal(models.Model):
     username = models.ForeignKey(User, on_delete=models.CASCADE)
     user_email = models.EmailField
     user_type = models.SmallIntegerField
     user_school = models.CharField
     user_contact = models.CharField
     user_regdate = models.DateField

class UserStudent(models.Model):
     username = models.ForeignKey(User, on_delete=models.CASCADE)
     user_type = models.ForeignKey(UserOptimum, on_delete=models.CASCADE)
     student_grade = models.SmallIntegerField # Matthayom 1, 2, 3
     student_class = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
'''