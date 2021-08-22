import paho.mqtt.client as mqtt
import time
import json
# from users.stock_handler import update_stock_prices
from app.helpers.orders.buy import buy_orders
from app.helpers.orders.sell import sell_orders
from app.helpers.stocks.update import update_stock_prices


# time.sleep(10)

def on_message(client, userdata, message):
    body = str(message.payload.decode("utf-8"))
    parsed_body = json.loads(body)
    buy_orders(parsed_body)
    sell_orders(parsed_body)
    update_stock_prices(parsed_body)


client = mqtt.Client() 
client.on_message=on_message 
client.connect('vernemq', 1883, 100)
client.loop_start() 
client.subscribe("thndr-trading")
