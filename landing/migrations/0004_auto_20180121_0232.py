# Generated by Django 2.0.1 on 2018-01-21 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20180118_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='quota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landing.Quota'),
        ),
    ]