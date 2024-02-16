from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)

class BlogAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')