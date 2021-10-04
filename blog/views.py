from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    model = Post


    def get_queryset(self):
        # Фильтруем посты по определённой категории, которая указана в url
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class HomeView(ListView):
    model = Post
    paginate_by = 8
    template_name = "blog/home.html"

# Create your views here.
