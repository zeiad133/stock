from django.http import JsonResponse, HttpResponse
from users.models import User
from users.serializers import UserSerializer, StockSerializer
import json
from django.core.cache import cache

def order_helper(request_body, request_type):
    body = json.loads(request_body)
    body = {
    'user_id': body.get('user_id'),
    'stock_id': body.get('stock_id'),
    'upper_bound': body.get('upper_bound'),
    'lower_bound': body.get('lower_bound'),
    'total': body.get('total'),
  }

    old_orders = cache.get(request_type)
    if not old_orders: 
      cache.set(request_type, [body])
    else:
      cache.set(request_type, old_orders + [body])

def buy(request):
  order_helper(request.body, 'orders_to_buy')
  return JsonResponse('Your request has been done', safe=False)


def sell(request):
  order_helper(request.body, 'orders_to_sell')
  return JsonResponse('Your request has been done', safe=False)
  