# Generated by Django 3.1.7 on 2021-04-12 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('source', '0005_auto_20210412_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='upload_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to=settings.AUTH_USER_MODEL),
        ),
    ]
