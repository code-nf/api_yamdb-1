from rest_framework import viewsets
from reviews.models import Categories
from .serializers import CategoriesSerializer
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters


class WithoutPatсhPutViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    pass


class CategoriesViewSet(WithoutPatсhPutViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'slug'
    # пагинация
    # поиск по слагу?
