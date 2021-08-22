from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.serializers.stock import StockSerializer

from django.core.cache import cache

@api_view(['GET'])
def show(request, id):
  stock = cache.get(id)
  if not stock: 
    return Response('Stock not found', status= 404)

  return Response(StockSerializer.new(stock))
  