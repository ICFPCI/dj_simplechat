# Generated by Django 5.0.4 on 2024-04-10 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_user_conversation_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='modified_at',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='modified_at',
            new_name='modified',
        ),
    ]