# Generated by Django 5.0.4 on 2024-05-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_conversation_is_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
