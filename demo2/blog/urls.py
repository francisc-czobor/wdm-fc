from django.urls import path

from .views.new_post import NewPostView
from .views.post_list import PostListView
from .views.index import IndexView
from .views.post_details import PostDetailsView
from .views.registration import RegistrationView
from .views.login import LoginView
from .views.logout import LogoutView

app_name = 'blog'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/<slug>', PostDetailsView.as_view(), name='post-details'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('new/', NewPostView.as_view(), name='new-post'),
    path('', IndexView.as_view(), name='index'),
]
