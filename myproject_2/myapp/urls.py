# 📄 urls.py – POST URL 연결  
from django.urls import path
from .views import receive_post

urlpatterns = [
    path('post/', receive_post),
]
