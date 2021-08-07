import paho.mqtt.client as mqtt
import time
import json
from polls.orders_handler import buy_orders, sell_orders
from polls.stock_handler import update_stock_prices

time.sleep(10)

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
