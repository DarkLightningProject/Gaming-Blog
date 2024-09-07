from django.urls import path
from .import views
from .views import index, like_post, dislike_post


urlpatterns = [
    path('blog/',views.index,name='blog-index'),
    path('like/<int:post_id>/', like_post, name='like-post'),
    path('dislike/<int:post_id>/', dislike_post, name='dislike-post'),
    path('post_detail/<int:pk>/',views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/',views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/',views.post_delete, name='blog-post-delete'),
   
   
]