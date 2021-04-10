from django.conf.urls import url

from . import views

app_name = "source"

urlpatterns = [
    url('list/', views.source_list, name='list'),

]
