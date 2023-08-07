import datetime

from django.db.models import Sum
from rest_framework.views import APIView
from .villagers_collection_serializer import VillagerCollectionSerializer
from rest_framework.response import Response
from rest_framework import status
from home.villagersCollection.villagers_collection_models import VillagersCollectionModel


class VillagersCollectionView(APIView):

    def post(self, request):
        serializer = VillagerCollectionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        admin = self.request.query_params.get("admin_id", "")
        year = self.request.query_params.get("year", datetime.datetime.now().year)
        villagers = VillagersCollectionModel.objects.filter(admin_id=admin, year=year)
        serializer = VillagerCollectionSerializer(villagers, many=True)
        return Response(serializer.data)

#Sum villagers collection data
    # def get(self, request):
    #     a=0.00
    #     admin = self.request.query_params.get("admin_id", "")
    #     year = self.request.query_params.get("year", datetime.datetime.now().year)
    #     villagers = VillagersCollectionModel.objects.filter(admin_id=admin, year=year)
    #     for i in villagers:
    #         a =a+float(i.collected_amount)
    #         print(a + float(i.collected_amount))
    #
    #     return Response(a)
