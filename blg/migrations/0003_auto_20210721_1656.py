# Generated by Django 3.1.6 on 2021-07-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0002_blogapps_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogapps',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/'),
        ),
    ]
