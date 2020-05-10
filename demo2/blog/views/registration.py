from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


class RegistrationView(View):
    @classmethod
    def get(cls, request):
        return render(request, 'registration.html')

    @classmethod
    def post(cls, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)

        return HttpResponseRedirect(reverse('blog:index'))
