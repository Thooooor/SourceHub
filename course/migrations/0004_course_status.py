# Generated by Django 3.1.7 on 2021-04-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210411_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default='open', max_length=128),
        ),
    ]
