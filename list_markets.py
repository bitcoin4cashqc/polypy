from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs,OrderType
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY,SELL
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

HOST = "https://clob.polymarket.com"
CHAIN_ID = POLYGON
# Private key we exported from polymarket UI
KEY = os.getenv("PK")
# Funder we got from polymarket UI
FUNDER = os.getenv("funder")

# Create CLOB client and get/set API credentials
client = ClobClient(
    HOST,
    key=KEY,
    chain_id=CHAIN_ID,
    funder=FUNDER,
    signature_type=1,
)
client.set_api_creds(client.create_or_derive_api_creds())

closed = "false"
active = "true"
limit = 100
tag = "bitcoin"
markets = requests.get(f"https://gamma-api.polymarket.com/markets?tag={tag}&limit={limit}&closed={closed}&active={active}")
#print(markets.json())


json_data = json.dumps(markets.json(), indent=4)
with open(f"markets_{tag}.json", "w") as file:
    file.write(json_data)
print(f"Data formatted and saved to markets_{tag}.json")


# events = requests.get("https://gamma-api.polymarket.com/events")
# print(events.json())


# json_data = json.dumps(events.json(), indent=4)
# with open("events.json", "w") as file:
#     file.write(json_data)
# print("Data formatted and saved to events.json")


#price = we offer 0.10$ to win $1
#size = we do that 10x, so $1 to win $10
#side = BUY or SELL



