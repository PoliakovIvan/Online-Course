from django.urls import path
from apps.courses.views import CourseListView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)