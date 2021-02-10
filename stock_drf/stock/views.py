from django.shortcuts import render

from stock.models import Stock
from rest_framework import viewsets, permissions

from stock.serializers import StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    