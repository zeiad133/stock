from rest_framework import serializers
from app.models.user_stock import UserStock

class UserStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStock
        fields = ['stock_name', 'stock_id', 'total']