from django.urls import path
from . import views

urlpatterns = [
    path("calculationsheets/", views.calculationsheets, name="calculationsheets")
]