# Generated by Django 3.1.6 on 2021-07-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogapps',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]