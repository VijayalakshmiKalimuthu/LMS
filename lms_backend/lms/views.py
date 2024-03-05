from django.shortcuts import render
from rest_framework import generics
from .models import Login
from .serializers import LoginSerializer

class LoginListCreateAPIView(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class LoginRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

