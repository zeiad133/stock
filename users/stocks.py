from django.http import JsonResponse
from users.serializers import StockSerializer
from django.core.cache import cache
import json



def stockView(request):
  json_data = json.loads(request.body)
  stock_id = json_data.get('stock_id')
  stock = cache.get(stock_id)
  if not stock: 
    return JsonResponse('Stock not found', safe = False, status= 404)

  return JsonResponse(StockSerializer(stock), safe=False)
  