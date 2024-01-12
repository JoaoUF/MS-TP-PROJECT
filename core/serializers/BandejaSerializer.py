from rest_framework import serializers
from core.models import Bandeja


class BandejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeja
        fields = '__all__'
