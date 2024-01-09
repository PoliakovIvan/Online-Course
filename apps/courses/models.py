from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.teachers.models import Teacher

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_info = models.TextField()
    start_date = models.DateField()
    course_duration = models.IntegerField()
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
    teachers = models.ManyToManyField(Teacher, related_name='courses')


    def __str__(self):
        return self.course_name
