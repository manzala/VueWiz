from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', include('VueWiz.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
