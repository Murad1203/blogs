# Generated by Django 3.1.6 on 2021-08-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0003_auto_20210721_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogapps',
            options={'ordering': ['-created_at'], 'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterField(
            model_name='blogapps',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='blogapps',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
    ]
