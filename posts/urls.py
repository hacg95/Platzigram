"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts.views import PostsFeedView, CreatePostView, PostDetailView

urlpatterns = [

    path(
        route='',
        view=PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=CreatePostView.as_view(),
        name='new_post'
    ),

    path(
        route='posts/<int:pk>/',
        view=PostDetailView.as_view(),
        name='detail'
    )
]