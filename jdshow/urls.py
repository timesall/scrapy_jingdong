from django.conf.urls import url
from .views import index,phone_info,reg_login


urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^(?P<product_id>\d+)/$', phone_info,name='product'),
    url(r'^reglogin$', reg_login),
]
