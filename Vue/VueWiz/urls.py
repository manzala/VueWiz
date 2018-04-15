from django.conf.urls import url

from . import views

from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^done', views.done, name='done'),
    url(r'^error', views.error, name='error'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^signin', views.signin, name='signin'),
    url(r'^upload', views.upload, name='upload')

] 
