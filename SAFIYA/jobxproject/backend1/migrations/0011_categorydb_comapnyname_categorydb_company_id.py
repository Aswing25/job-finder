# Generated by Django 5.0.1 on 2024-01-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0010_companydb_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorydb',
            name='comapnyname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categorydb',
            name='company_id',
            field=models.IntegerField(null=True),
        ),
    ]