from django.conf.urls import url
from .views import (
    UserCreateApiView,
    UserLoginApiView
)

urlpatterns = [
    url('^login/$', UserLoginApiView.as_view(), name='register'),
    url('^register/$', UserCreateApiView.as_view(), name='login'),

]