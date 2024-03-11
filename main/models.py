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
