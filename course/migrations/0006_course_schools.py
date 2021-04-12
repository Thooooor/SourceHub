# Generated by Django 3.1.7 on 2021-04-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('course', '0005_auto_20210411_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='schools',
            field=models.ManyToManyField(blank=True, related_name='courses', to='school.School'),
        ),
    ]
