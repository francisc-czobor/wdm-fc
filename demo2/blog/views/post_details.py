from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.post import Post
from ..models.comment import Comment
from ..forms.comment_form import CommentForm


class PostDetailsView(LoginRequiredMixin, View):
    login_url = '/login/'

    @classmethod
    def get(cls, request, slug):
        return render(request, 'post_details.html', context={
            'post': Post.objects.get(slug=slug),
            'form': CommentForm(),
        })

    @classmethod
    def post(cls, request, slug):
        post = Post.objects.get(slug=slug)
        Comment(
            author=request.POST.get('author', ''),
            content=request.POST.get('content', ''),
            post=post,
        ).save()

        return HttpResponseRedirect(post.get_absolute_url())
