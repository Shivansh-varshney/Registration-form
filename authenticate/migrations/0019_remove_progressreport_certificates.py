# Generated by Django 5.0.2 on 2024-06-17 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0018_rename_subject33_subject_mark_subject3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progressreport',
            name='certificates',
        ),
    ]
