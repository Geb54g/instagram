from django.shortcuts import render
from .models import post
from django.views.generic import(
    ListView
)
# Create your views here.

class postListView(ListView):
    template_name="instagramApp/post.html"
    queryset=post.objects.all()
    context_object_name='posts'