from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from reviews.models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'bio', 'first_name',
            'last_name', 'email', 'role')


class NotAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')
        read_only_fields = ('role',)


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
