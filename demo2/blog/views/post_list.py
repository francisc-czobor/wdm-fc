from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.post import Post


class PostListView(LoginRequiredMixin, View):
    login_url = '/login/'

    @classmethod
    def get(cls, request):
        return render(request, 'post_list.html', context={
            'posts': Post.objects.all().order_by('-created_at'),
        })
