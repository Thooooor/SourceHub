# Generated by Django 3.1.7 on 2021-04-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='status',
            new_name='course_status',
        ),
    ]