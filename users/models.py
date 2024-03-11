from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    is_superuser = models.BooleanField(default=False, verbose_name='админ')
    is_staff = models.BooleanField(default=False, verbose_name='сотрудник')
    is_active = models.BooleanField(default=True, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Пользователь: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
