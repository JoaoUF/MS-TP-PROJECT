from rest_framework import serializers
from core.models import Universidad


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = '__all__'
