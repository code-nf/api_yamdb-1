from rest_framework import viewsets
from reviews.models import Categories, Genres, Titles
from .serializers import CategoriesSerializer, GenreSerializer, TitlesReadSerializer, TitlesWriteSerializer
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class WithoutPatсhPutViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    pass


class CategoriesViewSet(WithoutPatсhPutViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)
    # пагинация


class GenreViewSet(WithoutPatсhPutViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)
    # пагинация


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name','category__slug', 'genre__slug', 'year')

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return TitlesWriteSerializer

        return TitlesReadSerializer