from django.urls import path

from . import views

urlpatterns = [
    path("suggestions/", views.suggestions, name="suggestions"),
    path("set_progress/", views.set_progress, name="set_progress"),
    path("update_progress/", views.update_progress, name="update_progress"),
]
