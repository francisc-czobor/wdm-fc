from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import logout


class LogoutView(LoginRequiredMixin, View):
    login_url = '/login/'

    @classmethod
    def get(cls, request):
        logout(request)
        return HttpResponseRedirect(reverse('blog:index'))
