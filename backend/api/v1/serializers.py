from rest_framework import serializers
from shop.models import Product, SupplierCategory, Category, Supplier, Attribute, CatalogProduct, ProductAttribute
from users.models import Favorites


class CategoriesSerializer(serializers.ModelSerializer):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = tuple([field.name for field in model._meta.fields if field.name not in ('parent_category',)]) \
                 + ('parent_category',)

    def get_parent_category(self, obj):
        if obj.parent_category is not None:
            return CategoriesSerializer(obj.parent_category).data
        else:
            return None


class CategoriesNoDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CatalogProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CatalogProduct


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Supplier


class SupplierCategorySerializer(serializers.ModelSerializer):
    app_category = CategoriesNoDeptSerializer()
    supplier = SuppliersSerializer()

    class Meta:
        fields = '__all__'
        model = SupplierCategory


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Attribute


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        fields = '__all__'
        model = ProductAttribute


class ProductsSerializer(serializers.ModelSerializer):
    app_category = CategoriesNoDeptSerializer()
    category = SupplierCategorySerializer()
    catalog_product = CatalogProductSerializer()
    supplier = SuppliersSerializer()
    attribute = serializers.SerializerMethodField()

    class Meta:
        exclude = ()
        model = Product
        fields = tuple([field.name for field in model._meta.fields if field.name not in ('category', 'gender')]) \
                 + ('attribute', 'category')

    def get_attribute(self, instance):
        return ProductAttributeSerializer(
            instance.product_attr.all(), many=True, read_only=True).data


class FavoriteSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        request = self.context.get("request")
        return Favorites.objects.create(user=request.user, product_id=validated_data.get('product_id'))


class FavoriteGetSerializer(serializers.Serializer):
    product = serializers.SerializerMethodField()

    def get_product(self, instance):
        return ProductsSerializer(
            Product.objects.filter(id=instance.product_id), many=True, read_only=True).data
