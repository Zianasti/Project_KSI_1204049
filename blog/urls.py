from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
]