from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from ckeditor.fields import RichTextField

from django.utils import timezone


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    about = RichTextField()
    image = models.ImageField(upload_to='authors')

    def __str__(self):
        return self.name


class Post(models.Model):
    # TODO social author (mb use many to one)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')  # В деректории медиа создаём артиклс и там сохраняем
    text = models.TextField()
    category = models.ForeignKey(Category, related_name="post", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default='', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_recipes(self):
        return self.recipes.all()

    def get_comments(self):
        return self.comment.all()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    direction = RichTextField()
    post = models.ForeignKey(Post, related_name="recipes", on_delete=models.SET_NULL, null=True, blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
