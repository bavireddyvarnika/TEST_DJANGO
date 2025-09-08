from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_page, name="add_page"),          # renders the UI
    path("add-api/", views.add_numbers_api, name="add_numbers_api"),  # JSON API
]