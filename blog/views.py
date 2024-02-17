from django.shortcuts import render
from django.views import generic
from . forms import BlogForm
from . models import Blog, Comment



def post_blog(request):
    """ This function renders the blog form"""

    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect(reversed('home'))
    
    context = {
        'form': form
    }
    return render(request, 'blog/blog.html', context)


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6