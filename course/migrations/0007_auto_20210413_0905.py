# Generated by Django 3.1.7 on 2021-04-13 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('course', '0006_course_schools'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='schools',
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='school.school'),
        ),
    ]
