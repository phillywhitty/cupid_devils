from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Blog(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
    related_name="blog_post", null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    excerpt = models.TextField(blank=True)









