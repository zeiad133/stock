from rest_framework import serializers
from app.models.user import User
from app.serializers.user_stock import UserStockSerializer

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    stocks = UserStockSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['name', 'wallet', 'stocks']