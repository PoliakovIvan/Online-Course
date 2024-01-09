from .models import Course
from django.views.generic import ListView
from django.urls import reverse_lazy
from apps.teachers.models import Teacher
from django.shortcuts import render

class CourseListView(ListView):
    model = Course
    #success_url = reverse_lazy('coursespage:courses_list')
    template_name = 'courses/course_list.html'
    fields = ['corse_id','course_name', 'course_info', 'start_date', 'course_duration', 'course_price']

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # Отримати дані вчителів
            teachers = Teacher.objects.all()
            context['teachers'] = teachers  # Передати дані у контекст
            return context