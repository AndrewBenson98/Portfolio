# Generated by Django 3.2.7 on 2021-09-24 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_mainimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
