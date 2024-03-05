# urls.py
from django.urls import path
from .views import LoginListCreateAPIView, LoginRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('login/', LoginListCreateAPIView.as_view(), name='login-list-create'),
    path('login/<int:pk>/', LoginRetrieveUpdateDestroyAPIView.as_view(), name='login-retrieve-update-destroy'),
]
