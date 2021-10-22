from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Photo, Gallery
# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'get_image')
    readonly_fields = ('get_image', )
    prepopulated_fields = {'slug': ('name', )}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width={obj.image.width * 0.7} height={obj.image.height * 0.7}')


@admin.register(Gallery)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date')
