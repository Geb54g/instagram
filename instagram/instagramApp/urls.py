from django.urls import path,include
from .views import(
    postListView
)

app_name = 'instagramAPP'

urlpatterns=[
    path('',postListView.as_view(), name ='post'),
    # path('new/', PostCreateView.as_view(), name='post_create'),
    
]