from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView
)

from .models import Articles


class ArticleCreateView(CreateView):
    model = Articles
    fields = {
        'title',
        'body',
        'author'
    }
    template_name = 'article_new.html'

class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Articles
    fields = [
        'title',
        'body'
    ]
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy("article_list")