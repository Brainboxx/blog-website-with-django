from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    path('', views.post_list, name='post-list'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('about/', views.about, name='blog-about'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
