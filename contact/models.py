from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """ Класс модели обратной связи """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """ Класс модели страницы О нас """
    text = RichTextField()
    mini_text = RichTextField()

    def __str__(self):
        start = int(self.text.find('>')) + 1
        return self.text[start:50]

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]


class ImageAbout(models.Model):
    """ Класс моделей изображений О нас"""
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    alt = models.CharField(max_length=100)


class Social(models.Model):
    """ Класс моделей соц сетей страницы О нас """
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name
