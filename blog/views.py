from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from . forms import BlogForm, CommentForm, EditForm
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

    queryset = Blog.objects.filter(status=1)
    blog = get_object_or_404(queryset, pk=blog_id)
    comments = blog.comments.filter(approved=True).order_by("-created_on")

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()
            messages.success(request, 'Your comment has been uploaded for approval.')
            return redirect(reverse('blog_details', args=[blog_id]))
    else:
        comment_form = CommentForm()

    context = {
        "blog": blog,
        "comments": comments,
        "commented": True,
        "comment_form": comment_form
    }

    return render(request, "blog/blog_detail.html", context)


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


def edit_comment(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog_list'))

    else:
        form = CommentForm(instance=comment)
    context = {
        'form': form,
    }
    return render(request, 'blog/edit_comment.html', context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect(reverse('blog_list'))
