from django.urls import path

from .views import home, ceva, tabele

urlpatterns = [
    path('home/', home),
    path('tabele/', tabele),
    path('', ceva),
]
