from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.DateTimeField(verbose_name='время', **NULLABLE)
    action = models.CharField(max_length=250, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки', **NULLABLE)
    related_habit = models.ForeignKey('self', verbose_name='связанная привычка',
                                      on_delete=models.CASCADE, **NULLABLE
                                      )
    frequency = models.PositiveSmallIntegerField(default=1, verbose_name='периодичность',**NULLABLE)
    award = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(default=30, verbose_name='время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='публичность', **NULLABLE)

    def __str__(self):
        return f'{self.action}: {self.place}, {self.time}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
