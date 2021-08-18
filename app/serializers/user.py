from rest_framework import serializers
from app.models.user import User

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'wallet']