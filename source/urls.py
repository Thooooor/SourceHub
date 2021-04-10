from django.urls import path

from . import views

app_name = "source"

urlpatterns = [
    path('source-list/', views.source_list, name='source_list'),
    path('source-detail/<int:id>/', views.source_detail, name="source_detail"),
    path('source-post/', views.source_post, name="source_post"),
]
