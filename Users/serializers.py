from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from Users.models import Import_User

class RegisterSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=1000)
    ProfilePic = serializers.ImageField()
    Address = serializers.CharField(max_length=1000)
    Country = serializers.CharField(max_length=1000)
    State = serializers.CharField(max_length=1000)
    City = serializers.CharField(max_length=1000)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return Import_User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(max_length=1000)