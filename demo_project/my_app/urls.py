from django.urls import path

from .views import home, ceva, TabeleView

app_name = 'ceva'

urlpatterns = [
    path('tabele/', TabeleView.as_view(), name='tab'),
    path('', home, name='index'),
    # path('', ceva),
]

