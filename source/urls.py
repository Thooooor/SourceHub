from django.urls import path

from . import views

app_name = "source"

urlpatterns = [
    path('source-list/', views.source_list, name='source_list'),
    path('source-post/', views.source_post, name="source_post"),
    path('source-delete/<int:id>/', views.source_delete, name="source_delete"),
    path('source-download-count', views.source_download_count, name="source_download_count"),

]
