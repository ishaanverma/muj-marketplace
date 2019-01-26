from rest_framework import serializers
from products.models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'first_name', 'last_name', 'user_products')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Product
        fields = ('url', 'id', 'title', 'description', 'price', 'image', 'category', 'user')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'name')
