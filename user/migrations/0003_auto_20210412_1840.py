# Generated by Django 3.1.7 on 2021-04-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210412_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_status',
            field=models.CharField(default='unread', max_length=128),
        ),
    ]
