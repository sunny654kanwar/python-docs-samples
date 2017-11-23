from django.conf.urls import url
from .views import sapcall

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^sapapi', sapcall, name='sapapi'),
]
