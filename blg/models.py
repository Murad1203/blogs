from django.db import models

# Create your models here.
from django.urls import reverse


class BlogApps(models.Model):

    title = models.CharField(max_length=20, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='Дата публикации')
    photo = models.ImageField(null=True, upload_to='photo/', verbose_name='Картинка')
    updated_at = models.DateTimeField(auto_now = True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')


    def get_absolute_url(self):
        return reverse('get_blog', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id':self.pk})

    def __str__(self):
        return self.title