from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_create')  # Отображаемые поля
    list_display_links = ('id', 'title')  # Поля в виде ссылки для перехода к конкретной записи
    search_fields = ('title',)  # Поля по которым можно производить поиск
    list_filter = ('date_create',)  # Поля по которым можно производить фильтрацию
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
