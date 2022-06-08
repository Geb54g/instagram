from django.urls import path,include
from .views import(
    PostListView,PostCreateView
)

app_name = 'instagramAPP'

urlpatterns=[
    path('',PostListView.as_view(), name ='post'),
    path('create/', PostCreateView.as_view(), name='create'),
    
]