# Generated by Django 5.0.3 on 2024-03-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телеграм'),
        ),
    ]
