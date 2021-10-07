from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index, name="index"),
    path("blogpost/<str:id>", views.blogpost, name="blogpost")
]
