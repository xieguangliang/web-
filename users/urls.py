from users import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^register/$', views.register),
    re_path(r'^login/$', views.LoginView.as_view())
    
]