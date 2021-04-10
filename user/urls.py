from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("sign-in/", views.user_sign_in, name="sign_in"),
    path("sign-up/", views.user_sign_up, name="sign_up"),
    path("info/", views.user_info, name="info"),
    path("message-detail/<int:id>/", views.message_detail, name="message_detail"),
]
