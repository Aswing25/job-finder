# Generated by Django 4.2.4 on 2023-12-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0005_clientdb_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdb',
            name='resume',
            field=models.FileField(upload_to='resume'),
        ),
    ]