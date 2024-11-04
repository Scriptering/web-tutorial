from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("steve/", views.steve, name="steve"),
    path("brian/", views.brian, name="brian"),
    path("<str:name>/", views.greet, name="greet")
]