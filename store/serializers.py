from rest_framework import serializers
from .models import User, Product, CartItem

# 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    '''write only, exists for swagger doc for user register'''
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    '''readonly, exists for swagger doc'''
    class Meta:
        model = User
        fields = ['username', 'password']

# 商品序列化器
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    # call methods
    total_price = serializers.ReadOnlyField()
    original_total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = '__all__'

# 购物车序列化器
class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    #user = serializers.ReadOnlyField()
    user = serializers.RelatedField(source='cart.user', read_only=True)

    class Meta:
        model = CartItem
        fields = ['user', 'product', 'quantity', 'total_price']

