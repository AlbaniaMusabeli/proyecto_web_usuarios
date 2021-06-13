#SERIALIZACION: tomar objetos de python y convertirlos a codigo javascript

#Importar la clase User
from django.contrib.auth.models import User
from django.db.models import fields

#Importar desde restframework los serializers
from rest_framework import serializers

#Crear una clase User
class UserSerializer(serializers.ModelSerializer):
    class Meta: #subclase meta: que cosas se van a utilizar dentro de la interfaz
        model = User
        fields = ("username","email")