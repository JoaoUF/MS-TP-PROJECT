from rest_framework import serializers
from core.models import TipoUsuario


class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'
