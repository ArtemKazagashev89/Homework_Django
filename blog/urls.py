from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('post/', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='blogpost_form'),
    path('post/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_confirm_delete'),
]