# from django.urls import path
# from .views import hello_world

# urlpatterns = [
#     # path('hello/', hello_world),
#     path('', hello_world),   
# ]
from django.urls import path
from .views import hello_world_post, csrf_token_view

urlpatterns = [
    path("hello-post/", hello_world_post),   # POST API
    path("csrf-token/", csrf_token_view),    # Endpoint to fetch CSRF token
]