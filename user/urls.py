from django.conf.urls import url

from . import views

app_name = "user"

urlpatterns = [
    url("info/", views.user_info, name="info"),
]
