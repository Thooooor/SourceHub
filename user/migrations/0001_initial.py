# Generated by Django 3.1.7 on 2021-04-10 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=128)),
                ('teacher_name', models.CharField(max_length=128)),
                ('courses', models.ManyToManyField(null=True, related_name='teachers', to='course.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-teacher_id',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=128)),
                ('student_name', models.CharField(max_length=128)),
                ('courses', models.ManyToManyField(null=True, related_name='students', to='course.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-student_id',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('send_time', models.TimeField(auto_now=True)),
                ('read_time', models.TimeField(null=True)),
                ('status', models.CharField(default='Unread', max_length=128)),
                ('receive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recv_message', to=settings.AUTH_USER_MODEL)),
                ('send', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='send_message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]