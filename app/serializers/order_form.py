from rest_framework import serializers

# Serializers define the API representation.


class OrderFormSerializer(serializers.Serializer):
  def validate(self, data):
    if data['lower_bound'] > data['upper_bound']:
        raise serializers.ValidationError({"Lower bound": "upper bound must greater than lower bound"})
    return data
  total = serializers.IntegerField(required=True, min_value= 1)
  upper_bound = serializers.IntegerField(required=True, min_value= 1)
  lower_bound = serializers.IntegerField(required=True, min_value= 1)
