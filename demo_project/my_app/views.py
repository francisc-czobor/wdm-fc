from django.shortcuts import render

from django.utils import timezone

# Create your views here.


def home(request):
    context = {
        'chestie': timezone.now().microsecond,
    }
    return render(request, template_name='home.html', context=context)
