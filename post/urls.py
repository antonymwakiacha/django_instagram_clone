from post.views import index, NewPost, PostDetails, tags, like
from django.urls import path

urlpatterns =[
    path('', index, name='index'),
    path('newpost/', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetails, name='postdetails'),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('<uuid:post_id>/like',like, name='postlike'),
]