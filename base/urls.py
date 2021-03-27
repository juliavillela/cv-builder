from django.urls import path
from .views import homepage, bootstrap

# base App urls
app_name = 'base'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('bootstrap/', bootstrap, name='bootstrap'),
]