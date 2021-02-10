from stock.models import Stock
from rest_framework import serializers

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
