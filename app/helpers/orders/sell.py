from app.models.user import User
from app.models.user_stock import UserStock
from app.models.order import Order

def sell_orders(stock):
  stock_id = stock.get('stock_id')
  current_price = stock.get('price')
  stock_availability = stock.get('availability')
  stock_name = stock.get('name')
  orders_to_sell = Order.objects.filter(
    stock_id=stock_id,
    lower_bound__lte=current_price,
    upper_bound__gte=current_price,
    total__lte=stock_availability,
    order_type='sell'
    )

  for order in orders_to_sell:
    user = User.objects.get(id=order.user_id)
    serve_order(user, stock_id, order, current_price)

def serve_order(user, stock_id, order, current_price):
    total_stocks = order.total
    user_stock = user.stocks.get(stock_id=stock_id)
    user_stock.stocks_on_hold -= order.total
    user.wallet += current_price * total_stocks
    user_stock.total -= total_stocks

    user.save()
    user_stock.save()
    if user_stock.total == 0: user_stock.delete()
    order.delete()

def user_has_enough_shares(user, stock, total):
  if not stock: return False
  return stock.total >= total
