from django.contrib.auth.models import User
from rest_framework import serializers

from PrimeraA.models import Equipo


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('nombre', 'ciudad', 'estadio')

    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Equipo.objects.create (**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.nombre = validated_data.get ('nombre', instance.nombre)
        instance.estadio = validated_data.get ('estadio', instance.estadio)
        instance.ciudad = validated_data.get ('ciudad', instance.ciudad)
        instance.save ()
        return instance