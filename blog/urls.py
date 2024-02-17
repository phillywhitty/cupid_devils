from django.urls import path
from . import views

urlpatterns = [
    path('post_blog/', views.post_blog, name='post_blog'),
    path("blog_list", views.BlogList.as_view(), name="blog_list"),
    path("<slug:slug>/", views.BlogDetail.as_view(), name="blog_detail"),
]