from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^done', views.done, name='done'),
    url(r'^error', views.error, name='error'),
    url(r'^signup', views.signup, name='signup'),
]