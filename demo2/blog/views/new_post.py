from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from ..models.post import Post
from ..forms.post_form import PostForm


class NewPostView(LoginRequiredMixin, View):
    login_url = '/login/'

    @classmethod
    def get(cls, request):
        return render(request, 'new_post.html', context={
            'form': PostForm()
        })

    @classmethod
    def post(cls, request):

        Post(
            title=request.POST['title'],
            author=request.POST['author'],
            content=request.POST['content'],
        ).save()

        return HttpResponseRedirect(reverse('blog:post-list'))
