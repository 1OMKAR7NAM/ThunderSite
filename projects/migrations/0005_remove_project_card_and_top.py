# Generated by Django 2.0.1 on 2018-04-16 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='card_and_top',
        ),
    ]