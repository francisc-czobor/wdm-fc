from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(View):
    @classmethod
    def get(cls, request):
        return render(request, 'login.html')

    @classmethod
    def post(cls, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
        else:
            print('aiurea')

        return HttpResponseRedirect(reverse('blog:index'))
