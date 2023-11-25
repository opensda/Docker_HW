from django.urls import path

from atomichabits.apps import AtomichabitsConfig
from atomichabits.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = AtomichabitsConfig.name


urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/", HabitListAPIView.as_view(), name="habit_list"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
