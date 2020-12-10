from helloworld import views
from django.urls import re_path

urlpatterns = [
    re_path(r'helloworld/$', views.first_view_func)
]