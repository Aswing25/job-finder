# Generated by Django 4.2.4 on 2023-12-01 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0003_rename_resume_resumedb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResumeDb',
        ),
    ]
