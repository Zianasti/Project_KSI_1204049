from django.urls import path, re_path
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    re_path(r'^delete/(?P<delete_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^create/$', views.create, name='create'),
    url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
    re_path(r'^update/(?<update_id>[0-9]+)/$', views.update, name='update'),
]