from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_product),
    path('echo', views.echo),
    path('hello', views.hello_world)
]