from django.urls import path
from . import views

urlpatterns = [
    path('post_blog/', views.post_blog, name='post_blog'),
    path('<int:blog_id>/', views.post_comment, name='post_comment'),
    path("blog_list/", views.BlogList.as_view(), name="blog_list"),
    path("<int:blog_id>/", views.blog_details, name="blog_details"),
    path('like/<int:blog_id>/', views.BlogLike.as_view(), name='blog_like'),
    path('<int:pk>/delete_comment/',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('<int:pk>/edit_comment/',
         views.CommentEdit.as_view(), name="edit_comment"),

]