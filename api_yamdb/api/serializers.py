from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from reviews.models import User, Category, Genre, Title
import datetime as dt
from reviews.validators import validate_username


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
    email = serializers.EmailField(
        required=True,
        max_length=254,)
    username = serializers.CharField(
        required=True,
        validators=[validate_username],
        max_length=150)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitlesWriteSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug', many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')

    def get_rating(self, obj):

        pass


class TitlesReadSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenreSerializer(many=True)
    category = CategoriesSerializer()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')

    def validate_year(self, value):
        year = dt.date.today().year
        if not (value <= year):
            raise serializers.ValidationError(
                'Год произведения указан некорректно!')
        return value

    def get_rating(self, obj):
        pass
