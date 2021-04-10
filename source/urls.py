from django.urls import path

from . import views

app_name = "source"

urlpatterns = [
    path('list/', views.source_list, name='list'),

]
