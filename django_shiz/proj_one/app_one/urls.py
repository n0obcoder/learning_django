from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name = 'index'), # index in views.index is the name of the function
]
