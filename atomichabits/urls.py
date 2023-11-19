from django.urls import path

from atomichabits.apps import AtomichabitsConfig
from atomichabits.views import CourseCreateAPIView

app_name = AtomichabitsConfig.name



urlpatterns = [
    path("course/create/", CourseCreateAPIView, name="course_create")
]