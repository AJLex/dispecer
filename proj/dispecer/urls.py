from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.current_info, name='current info'),    
]
