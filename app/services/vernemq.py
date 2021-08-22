import paho.mqtt.client as mqtt
import time
import json
from app.helpers.orders.buy import buy_orders
from app.helpers.orders.sell import sell_orders
from app.helpers.stocks.update import update_stock_prices
import environ
env = environ.Env()
base = environ.Path(__file__) - 3
environ.Env.read_env(env_file=base('.env'))


def on_message(client, userdata, message):
    body = str(message.payload.decode("utf-8"))
    parsed_body = json.loads(body)
    buy_orders(parsed_body)
    sell_orders(parsed_body)
    update_stock_prices(parsed_body)

def connect():
  client = mqtt.Client() 
  client.on_message=on_message
  try:
    client.connect(env.str('VERNEMEQ_HOST'), env.int('VERNEMEQ_PORT'), 100)
    client.loop_start() 
    client.subscribe("thndr-trading")
  except:
    time.sleep(3)
    connect()
connect()
