from rest_framework import serializers
from .villagers_models import VillagersModel

class VillagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillagersModel
        fields = '__all__'
