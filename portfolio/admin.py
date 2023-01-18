from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_title = 'Portfolio'
admin.site.site_header = 'Админ-панель Сайта Портфолио'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_image')  # Отображаемые поля
    list_display_links = ('id', 'title')  # Поля в виде ссылки для перехода к конкретной записи
    search_fields = ('id', 'title')  # Поля по которым можно производить поиск
    readonly_fields = ('get_html_image',)
    fields = ('title', 'description', 'get_html_image', 'image', 'url')

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=75>")
        else:
            return "Нет фото"

    get_html_image.short_description = "Миниатюра"


admin.site.register(Project, ProjectAdmin)
