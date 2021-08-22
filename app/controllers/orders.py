from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models.user import User
from app.models.user_stock import UserStock
from app.models.order import Order
from app.serializers.order_form import OrderFormSerializer

@api_view(['POST'])
def buy(request, id, stock_id):
  body = request.data

  validation = OrderFormSerializer(data=body)
  if not validation.is_valid(): return  Response(validation.errors, status=400)

  user = User.objects.get(id=id)
  user.money_on_hold += int(body.get('total')) * int(body.get('upper_bound'))
  user.save()
  insert_order(body, id, stock_id, 'buy')
  return Response("Your order has been done")

@api_view(['POST'])
def sell(request, id, stock_id):
  body = request.data

  validation = OrderFormSerializer(data=body)
  if not validation.is_valid(): return  Response(validation.errors, status=400)

  user_stock = UserStock.objects.get(user_id=id, stock_id= stock_id)
  user_stock.stocks_on_hold += int(body.get('total'))
  user_stock.save()
  insert_order(body, id, stock_id, 'sell')
  return Response("Your order has been done")

def insert_order(body, user_id, stock_id, request_type):

  new_order = Order(
    user_id=user_id,
    stock_id= stock_id,
    upper_bound=body.get('upper_bound'),
    lower_bound=body.get('lower_bound'),
    total = body.get('total'),
    order_type= request_type
    )
  new_order.save()