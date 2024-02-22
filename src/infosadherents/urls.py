from django.urls import path
from . import views

app_name = 'infoadherents'

urlpatterns = [
    path('', views.index, name="home"),
]