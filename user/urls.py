from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("sign-in/", views.user_sign_in, name="sign_in"),
    path("sign-up/", views.user_sign_up, name="sign_up"),
    path("sign-out/", views.user_sign_out, name="sign_out"),
    path("user-info/<int:id>/", views.user_info, name="user_info"),
    path("message-post/", views.message_post, name="message_post"),
    path("message-detail/<int:id>/", views.message_detail, name="message_detail"),
]
