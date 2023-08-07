from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserRegistrationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import UserRegistration
from rest_framework import status


@api_view(["POST"])
def UserData(request):
    serializer = UserRegistrationSerializer(data=request.data)
    # reponse = UserRegistrationSerializerReponse(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": serializer.data})
    return Response({"message": "test"})


class RegistrationList(ListModelMixin, GenericAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

    def list(self, request, *args, **kwargs):
        queryset = UserRegistration.objects.filter(name=request.data['name'])
        serializer = UserRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def GetUser(request):
    querySet = UserRegistration.objects.all()
    serializer = UserRegistrationSerializer(
        querySet.filter(name=request.data["name"], password=request.data["password"]), many=True)
    try:
        return Response(serializer.data[0])
    except:
        return Response("Something else", status=status.HTTP_404_NOT_FOUND)
