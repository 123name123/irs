# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attribute(models.Model):
    title = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'attribute'


class CatalogProduct(models.Model):
    title = models.CharField(max_length=256)
    upc = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=32, blank=True, null=True)
    model = models.CharField(max_length=128, blank=True, null=True)
    images = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'catalog_product'


class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    sort_code = models.CharField(max_length=2)
    name = models.TextField()
    category_level = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField(blank=True, null=True)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

class Supplier(models.Model):
    name = models.TextField()
    site_url = models.TextField()
    display_name = models.TextField()
    is_active = models.BooleanField()
    image = models.CharField(max_length=255, blank=True, null=True)
    type = models.TextField()  # This field type is a guess.
    region = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'supplier'


class SupplierCategory(models.Model):
    name = models.TextField()
    supplier_category_id = models.CharField(max_length=64, blank=True, null=True)
    supplier_parent_category_id = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField()
    category_url = models.CharField(max_length=512, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    matched_manually = models.BooleanField(blank=True, null=True)
    processed_by_human = models.BooleanField()
    category_level = models.SmallIntegerField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    dont_monitor_products = models.BooleanField()
    app_category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplier_category'
        unique_together = (('supplier', 'supplier_category_id'),)

class Product(models.Model):
    item_id = models.CharField(max_length=64)
    title = models.CharField(max_length=256)
    upc = models.CharField(max_length=32, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promotion_message = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.TextField()
    page_number = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=32, blank=True, null=True)
    model = models.CharField(max_length=128, blank=True, null=True)
    is_low_stock = models.BooleanField(blank=True, null=True)
    on_hand_inventory = models.IntegerField(blank=True, null=True)
    limit_quantity = models.IntegerField(blank=True, null=True)
    matched_manually = models.BooleanField(blank=True, null=True)
    processed_by_human = models.BooleanField()
    model_recognized = models.CharField(max_length=128)
    is_available = models.BooleanField()
    item_availability = models.CharField(max_length=19)
    reclassified_by = models.CharField(max_length=1)
    created_time = models.DateTimeField()
    quick_product_revision_time = models.DateTimeField(blank=True, null=True)
    full_product_revision_time = models.DateTimeField(blank=True, null=True)
    stock_status = models.CharField(max_length=1)
    app_category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    catalog_product = models.ForeignKey(CatalogProduct, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(SupplierCategory, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING)
    breadcrumbs = models.TextField(blank=True, null=True)  # This field type is a guess.
    images = models.TextField(blank=True, null=True)  # This field type is a guess.
    nutritional = models.JSONField(blank=True, null=True)
    specification = models.JSONField(blank=True, null=True)
    brand_recognized_id = models.IntegerField(blank=True, null=True)
    keywords = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('item_id', 'supplier'),)


class ProductAttribute(models.Model):
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING, related_name='product_attr')
    value = models.CharField(max_length=256)
    product = models.ForeignKey(Product, models.DO_NOTHING, related_name='product_attr')

    class Meta:
        managed = False
        db_table = 'product_attribute'
        unique_together = (('attribute', 'product'),)


