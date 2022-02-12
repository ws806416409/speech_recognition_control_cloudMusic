from django.urls import path, include
from server.views.index import index

urlpatterns = [
    path("", index, name="index"),
]