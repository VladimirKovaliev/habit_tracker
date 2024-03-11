from django.db import models

from config import settings

# Create your models here.

NULLABLE = {
    'null': True,
    'blank': True,
}

periods = (
    ('daily', 'Ежедневно'),
    ('weekly', 'Еженедельно'),
)


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='время', **NULLABLE)
    #флаг приятной привычки
    #связанная привычка FK
    #вознаграждение
    #время на выполнение timefield
    #время во сколько нужно выполнить задачу
    #дата datefield autonow для периодической задачи
    #периодичность
    #признак публичности


    def __str__(self):
        return f'owner:{self.owner}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
