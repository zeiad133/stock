# from users.models import User


# def UserSerializer(user):
#    return {
#       'id': user.id,
#       'name': user.name,
#       'stocks': UserStocksSerializer(user.stocks()),
#       'wallet': user.wallet}

# def UserStockSerializer(stock):
#   return {'name': stock.stock_name, 'id': stock.stock_id, 'total': stock.total}

# def UserStocksSerializer(stocks):
#   result = map(lambda stock: UserStockSerializer(stock), stocks)
#   return list(result)

# def StockSerializer(stock):
#   return {
#     'name': stock.get('name'),
#     'availability': stock.get('availability'),
#     'lowest_price_today': stock.get('lowest_price_today'),
#     'highest_price_today': stock.get('highest_price_today'),
#     'lowest_price_this_hour': stock.get('lowest_price_this_hour'),
#     'highest_price_this_hour': stock.get('highest_price_this_hour'),
#     }
  