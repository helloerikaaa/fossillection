from django.urls import path

from . import views

urlpatterns = [
    path('', views.fossil_view, name='index'),
]