# Generated by Django 2.0.1 on 2018-02-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180204_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cover_image',
            field=models.ImageField(default='', upload_to='news_cover'),
            preserve_default=False,
        ),
    ]
