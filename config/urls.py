from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls

from delivery.views import FoodViewSet, OrderViewSet
from user import views as user_views

router = routers.DefaultRouter()
router.register('foods', FoodViewSet, basename='foods')
router.register('orders', OrderViewSet, basename='orders')
router.register('users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
] + debug_toolbar_urls()

urlpatterns += router.urls
