from django.urls import path,include
from .views import(
    postListView,PostCreateView
)

app_name = 'instagramAPP'

urlpatterns=[
    path('',postListView.as_view(), name ='post'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    
]