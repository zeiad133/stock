from users.models import User, UserStocks
from django.core.cache import cache
import json

def buy_orders(stock):
  orders_to_buy = cache.get('orders_to_buy')
  if not orders_to_buy: return
  stock_id = stock.get('stock_id')
  for order in orders_to_buy:
      print(stock_id)
      print(order.get('stock_id'))
      if stock_id != order.get('stock_id'): continue

      user = User.objects.filter(id=order.get('user_id')).first()
      user_stock = user.stocks().filter(stock_id=stock_id).first()
      # print('aaaaaaaaaaaaaaaaaaaaaa')
      print(valid_to_buy(user, order, stock))
      if valid_to_buy(user, order, stock):
        if not user_stock: 
          user_stock  = create_user_stock(user.id, stock_id, stock.get('name'), total= order.get('total'))

        user.wallet -= stock.get('price') * order.get('total')
        user_stock.total += order.get('total')
        reflect_order(user, user_stock, 'orders_to_buy', order)

def sell_orders(stock):
  orders_to_sell = cache.get('orders_to_sell')
  if not orders_to_sell: return
  stock_current_price = stock.get('price')
  stock_id = stock.get('stock_id')
  if not orders_to_sell: return
  for order in orders_to_sell:
    if stock_id != order.get('stock_id'): continue
    user = User.objects.filter(id=order.get('user_id')).first()
    user_stock = user.stocks().filter(stock_id=stock_id).first()

    if valid_to_sell(user,user_stock,order,stock_current_price):
      user.wallet += stock_current_price * order.get('total')
      user_stock.total -= order.get('total')
      reflect_order(user, user_stock, 'orders_to_sell', order)

def valid_to_buy(user, order, stock):
    stock_current_price = stock.get('price')
    stock_availability = stock.get('availability')
    valid_price_range = price_within_range(stock_current_price, order)
    has_fund = user_has_fund(stock_current_price, user)
    return has_fund & valid_price_range & stock_has_enough_shares_to_buy(order, stock_availability)

def valid_to_sell(user,user_stock,order,stock_current_price):
    enough_shares = user_has_enough_shares(user,user_stock, order.get('total'))
    valid_price_range = price_within_range(stock_current_price, order)
    return enough_shares & valid_price_range

def create_user_stock(user_id, stock_id, stock_name, total):
  user_stock = UserStocks( user_id= user_id, stock_id=stock_id, stock_name=stock_name, total= total )
  user_stock.save()
  return user_stock




def reflect_order(user, user_stock, order_type, current_order):
      user.save()
      user_stock.save()
      orders = cache.get(order_type)
      orders.remove(current_order)
      cache.set(order_type, orders)

def user_has_enough_shares(user, stock, total):
  if not stock: return False
  return stock.total >= total


def stock_has_enough_shares_to_buy(order, availability):
    return order.get('total') <= availability

def price_within_range(current_price, order):
  return current_price <=order.get('upper_bound') and current_price >= order.get('lower_bound')

def user_has_fund(current_price, user):
    if not user: return False
    return user.wallet >= current_price
