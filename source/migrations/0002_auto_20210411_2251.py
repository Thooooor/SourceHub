# Generated by Django 3.1.7 on 2021-04-11 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='file',
            new_name='source_file',
        ),
    ]
