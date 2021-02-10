from django.contrib import admin
from django.urls import path, include
from stock import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
