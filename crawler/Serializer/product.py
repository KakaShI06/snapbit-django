from rest_framework import serializers
from crawler.models.Product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['id', 'name', 'created_at', 'updated_at', 'current_price', 'lowest_price', 'highest_price']