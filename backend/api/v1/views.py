from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action, api_view
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.models import Product, Category, Supplier
from users.models import Favorites
from . import serializers
from .filters import ProductsFilter, CategoriesFilter


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (Product.objects.select_related('app_category').
                select_related('catalog_product').
                select_related('category').
                select_related('supplier').
                all())
    serializer_class = serializers.ProductsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = ProductsFilter


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoriesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoriesFilter


class SuppliersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SuppliersSerializer


class FavoritesViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(self.get_queryset(), product_id=self.kwargs['pk'])

    def get_queryset(self):
        return self.request.user.favorites.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.FavoriteGetSerializer
        return serializers.FavoriteSerializer
