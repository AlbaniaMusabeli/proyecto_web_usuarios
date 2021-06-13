from django.shortcuts import render
from django.contrib.auth.models import User
# Viewset: codigo python se encarga de la renderizacion de los elementos. ej. JSON
from rest_framework import viewsets
from core.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    #cosas que quiero que muestre el serializador cuando se haga la peticion a la API
    queryset = User.objects.all().order_by("-date_joined")
