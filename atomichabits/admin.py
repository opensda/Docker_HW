from django.contrib import admin

from atomichabits.models import Habit


# Register your models here.


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "is_pleasant",
        "related_habit",
        "frequency",
        "award",
        "time_to_complete",
        "is_public"
    )
