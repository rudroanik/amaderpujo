from rest_framework import serializers
from .models import UserRegistration


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        #exclude = ['password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

