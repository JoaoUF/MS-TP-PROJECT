from rest_framework import serializers
from core.models import Vivienda


class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = '__all__'
