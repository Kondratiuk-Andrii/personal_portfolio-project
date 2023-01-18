from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='portfolio/images/', verbose_name='Изображение')
    url = models.URLField(blank=True, verbose_name='Ссылка на проект')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:home')
