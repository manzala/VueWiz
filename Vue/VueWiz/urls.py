from django.conf.urls import url

from . import views

from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^done', views.done, name='done'),
    url(r'^error', views.error, name='error'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^signin', views.signin, name='signin'),
    url(r'^upload_resume', views.upload_resume, name='upload_resume'),
    url(r'^video', views.upload_video, name='upload_video'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^media/(?P<path>\w{0,100}.pdf)', views.media, name='media')
]
