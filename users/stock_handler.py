from django.core.cache import cache
from datetime import datetime


def price_today(price, parsed_time, cached_stock):
  if cached_stock.get('current_day') != parsed_time.day:
    highest_price_today = lowest_price_today = price
  else:
    highest_price_today = max(cached_stock.get('highest_price_today'), price)
    lowest_price_today = min(cached_stock.get('lowest_price_today'), price)

  return {'highest_price_today': highest_price_today, 'lowest_price_today': lowest_price_today}

def price_this_hour(price, parsed_time, cached_stock):
  if cached_stock.get('current_hour') != parsed_time.hour:
    highest_price_this_hour = lowest_price_this_hour = price
  else:
    highest_price_this_hour = max(cached_stock.get('highest_price_this_hour'), price)
    lowest_price_this_hour = min(cached_stock.get('lowest_price_this_hour'), price)

  return {'highest_price_this_hour': highest_price_this_hour, 'lowest_price_this_hour': lowest_price_this_hour}


def update_stock_prices(stock):
  stock_id = stock.get('stock_id')
  price = stock.get('price')
  cached_stock = cache.get(stock_id)
  parsed_time = datetime.strptime(stock.get('timestamp'), '%Y-%m-%d %H:%M:%S.%f')
  if not cached_stock: 
    cache.set(stock_id, default_stock_values(stock, parsed_time))
  else:
    cache.set(stock_id,{
      'name': stock.get('name'),
      'availability': stock.get('availability'),
      'lowest_price_today': price_today(price, parsed_time,cached_stock).get('lowest_price_today'),
      'highest_price_today': price_today(price, parsed_time, cached_stock).get('highest_price_today'),
      'lowest_price_this_hour': price_this_hour(price, parsed_time,cached_stock).get('lowest_price_this_hour'),
      'highest_price_this_hour': price_this_hour(price, parsed_time,cached_stock).get('highest_price_this_hour'),
      'current_day': parsed_time.day,
      'current_hour': parsed_time.hour
      })

  


def default_stock_values(stock, parsed_time):
    price = stock.get('price')
    return {
    'name': stock.get('name'),
    'availability': stock.get('availability'),
    'lowest_price_today': price,
    'highest_price_today': price,
    'lowest_price_this_hour': price,
    'highest_price_this_hour': price,
    'current_day': parsed_time.day,
    'current_hour': parsed_time.hour
    }
