from rest_framework import serializers
from reviews.models import Categories, Genres


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'
        lookup_field = 'slug'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'
        lookup_field = 'slug'
