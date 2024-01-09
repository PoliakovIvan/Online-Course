from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator



class Teacher(models.Model):
    teacherName = models.CharField(max_length=300)
    teacherPhoto = models.ImageField(upload_to='teacher_photos/')
    jobTitle = models.CharField(max_length=100, default='')
    teacherRating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    numStudents = models.PositiveIntegerField()
    numCourses = models.PositiveIntegerField()
    teacherInfo = models.TextField()
    #sotial media links
    facebookUrl = models.URLField(max_length=200)
    instagramUrl = models.URLField(max_length=200)
    linkedinUrl = models.URLField(max_length=200)

    def __str__(self):
        return self.teacherName