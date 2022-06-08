from django.shortcuts import render
from .models import post
from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView, CreateView)
from .forms import PostForm

from django.views.generic import(
    ListView, CreateView
)
# Create your views here.

class postListView(ListView):
    template_name="instagramApp/post.html"
    queryset=post.objects.all()
    context_object_name='posts'
    
class PostCreateView(CreateView):
    template_name = 'insta/create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)