from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 6



