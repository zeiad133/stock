from app.models.user import User
from app.models.user_stock import UserStock
from app.models.order import Order


def buy_orders(stock):
  stock_id = stock.get('stock_id')
  current_price = stock.get('price')
  stock_availability = stock.get('availability')
  stock_name = stock.get('name')

  orders_to_buy = Order.objects.filter(
    stock_id=stock_id,
    lower_bound__lte=current_price,
    upper_bound__gte=current_price,
    total__lte=stock_availability,
    order_type='buy'
    )
  for order in orders_to_buy:
      user = User.objects.get(id=order.user_id)
      total_stocks = order.total
      if stock_availability < total_stocks: continue

      serve_order(user, stock_id, order, stock_name, current_price)

def serve_order(user, stock_id, order, stock_name, current_price):
  total_stocks = order.total
  user_stock = user.stocks.get_or_create(
  user_id = user.id, stock_id= stock_id, stock_name=stock_name
  )[0]
  user.wallet -= current_price * total_stocks
  user.money_on_hold -= order.total * order.upper_bound
  user_stock.total += total_stocks
  user.save()
  user_stock.save()
  order.delete()