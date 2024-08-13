from rest_framework import serializers
from delivery import models
from user.serializers import CustomerSerializer


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'


class OrderItemWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = ['food', 'quantity']


class OrderItemReadSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)

    class Meta:
        model = models.OrderItem
        exclude = ['order']


class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = OrderItemWriteSerializer(many=True)

    class Meta:
        model = models.Order
        fields = [
            'delivery_address',
            'payment_method',
            'order_items',
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        order_items_data = validated_data.pop('order_items')
        order = models.Order.objects.create(
            **validated_data,
            customer=request.user
        )
        for order_item_data in order_items_data:
            models.OrderItem.objects.create(
                order=order,
                **order_item_data
            )
        return order


class OrderReadSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    order_items = OrderItemReadSerializer(many=True)
    total_amount = serializers.ReadOnlyField()
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = models.Order
        fields = [
            'id',
            'delivery_address',
            'payment_method',
            'order_items',
            'total_amount',
            'customer',
        ]
