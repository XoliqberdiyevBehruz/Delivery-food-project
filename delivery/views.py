from rest_framework import views, viewsets
from delivery import models, serializers


class FoodViewSet(viewsets.ModelViewSet):
    queryset = models.Food.objects.order_by('-id')
    serializer_class = serializers.FoodSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    read_serializer_class = serializers.OrderReadSerializer
    create_serializer_class = serializers.OrderCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.OrderCreateSerializer
        return serializers.OrderReadSerializer
