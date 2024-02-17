from django.urls import path
from . import views

urlpatterns = [
    path('post_blog/', views.post_blog, name='post_blog'),
    path("blog_list/", views.BlogList.as_view(), name="blog_list"),
    path("<int:blog_id>/", views.blog_details, name="blog_details"),
    path('like/<slug:slug>', views.BlogLike.as_view(), name='blog_like'),

]