# Generated by Django 3.1.7 on 2021-04-10 09:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=128)),
                ('source_name', models.CharField(max_length=128)),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2021, 4, 10, 9, 23, 38, 588095, tzinfo=utc))),
                ('download_counts', models.BigIntegerField()),
                ('file', models.FileField(upload_to='')),
                ('courses', models.ManyToManyField(related_name='sources', to='course.Course')),
                ('upload_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-source_id',),
            },
        ),
    ]