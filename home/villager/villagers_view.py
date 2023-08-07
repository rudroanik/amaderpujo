from rest_framework.views import APIView
from .villagers_serializer import VillagerSerializer
from rest_framework.response import Response
from rest_framework import status
from home.villager.villagers_models import VillagersModel


class Villagers(APIView):

    def post(self, request):
        serializer = VillagerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        admin = self.request.query_params.get("admin_id", "")
        villagers = VillagersModel.objects.filter(admin_id=admin)
        serializer = VillagerSerializer(villagers, many=True)
        return Response(serializer.data)
