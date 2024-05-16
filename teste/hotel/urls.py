from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("quartos/", views.quartos),
    path("checkin/", views.checkin),
]
