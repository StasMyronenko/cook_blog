from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):  # возможность добавлять фото прямо во время создания текстов на странице
    model = ImageAbout
    extra = 1  # количество рецептов


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name', )


@admin.register(About)  # Подключаем возможность добавлять фото прямо во время создания текстов на странице
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline, ]

    save_on_top = True  # что бы кнопка сохранения была сверху


admin.site.register(ContactLink)
admin.site.register(Social)
