from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, PhotoView
from .models import Post
from .forms import PostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name ='article_details.html'

class AddPostView(CreateView):
    model =  Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__' # not required because using form_class
    #fields =('photo', 'name')
class AddPhotoView(PhotoView):
    model =  Post
    template_name = 'add_photo.html'
    fields =('photo', 'name')