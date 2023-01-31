from rest_framework import serializers
from reviews.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'
        lookup_field = 'slug'