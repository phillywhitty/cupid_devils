from django.shortcuts import render
from . forms import BlogForm


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