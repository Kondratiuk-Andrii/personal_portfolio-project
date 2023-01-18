from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, blank=True, unique=True, db_index=True, verbose_name="url")
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'blog_slug': self.slug})
