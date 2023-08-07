from rest_framework import serializers
from .villagers_collection_models import VillagersCollectionModel


class VillagerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillagersCollectionModel
        fields = '__all__'


