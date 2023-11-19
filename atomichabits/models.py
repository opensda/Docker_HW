from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.DateTimeField(verbose_name='время')
    action = models.CharField(max_length=250, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки', **NULLABLE)
    related_habit = models.ForeignKey('self', verbose_name='связанная привычка',
                                      on_delete=models.CASCADE, **NULLABLE
                                      )
    frequency = models.PositiveSmallIntegerField(default=1, verbose_name='периодичность')
    award = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(verbose_name='публичность', **NULLABLE)
