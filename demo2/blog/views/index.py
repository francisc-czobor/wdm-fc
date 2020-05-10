from django.views import View
from django.shortcuts import render


class IndexView(View):
    @classmethod
    def get(cls, request):

        print(request.user.is_authenticated)

        return render(request, 'index.html', context={
            'ceva': 'da',
            'altceva': 'nu',
        })
