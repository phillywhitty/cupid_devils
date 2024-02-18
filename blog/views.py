from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import BlogForm, CommentForm
from . models import Blog, Comment



def post_blog(request):
    """ This function renders the blog form"""

    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect(reverse('blog_list'))
  
    context = {
        'form': form
    }
    return render(request, 'blog/blog.html', context)


def post_comment(request, blog_id):
    """ This function renders the comment form"""

    blog = get_object_or_404(Blog, pk=blog_id)
    blog_comment = None
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            blog_comment = form.save(commit=False)
            form.blog = blog
            form.user = request.user
            form.save()
        return redirect(reverse('blog_details', args=[blog_id]))

    context = {
        'comment_form': form
    }
    return render(request, 'blog/blog_detail.html', context)


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created_on")
    template_name = "blog_list.html"
    paginate_by = 6


def blog_details(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    liked = False
    if blog.likes.filter(id=request.user.id).exists():
        liked = True
    comments = blog.comments.filter(approved=True).order_by("-created_on")

    context = {
        'blog': blog,
        'liked': liked,
        'comments': comments
    }

    return render(request, 'blog/blog_detail.html', context)

#class BlogDetail(View):
#
#    def get(self, request, slug, *args, **kwargs):
#        blog = get_object_or_404(Blog, slug=slug)
#        comments = blog.comments.filter(approved=True).order_by("-created_on")
#        liked = False
#        if blog.likes.filter(id=self.request.user.id).exists():
#            liked = True
#
#        return render(
#            request,
#            "blog_detail.html",
#            {
#                "blog": blog,
#                "comments": comments,
#                "liked": liked
#            },
#        )


class BlogLike(LoginRequiredMixin, View):

    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)

        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_details', args=[blog_id]))