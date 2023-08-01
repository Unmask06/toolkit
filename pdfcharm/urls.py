from django.urls import path

from . import views

urlpatterns = [
    path("pdfcharm/", views.pdfcharm, name="pdfcharm"),
]