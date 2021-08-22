class StockSerializer:
  def new(stock):
    return {
      'name': stock.get('name'),
      'availability': stock.get('availability'),
      'lowest_price_today': stock.get('lowest_price_today'),
      'highest_price_today': stock.get('highest_price_today'),
      'lowest_price_this_hour': stock.get('lowest_price_this_hour'),
      'highest_price_this_hour': stock.get('highest_price_this_hour'),
      'current_price': stock.get('current_price'),

      }