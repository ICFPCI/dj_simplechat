# Generated by Django 5.0.4 on 2024-05-21 22:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_keking'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contacts',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]