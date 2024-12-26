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


resp = client.create_and_post_order(
    OrderArgs(
        price=0.10,
        size=10.0,
        side=BUY,
        token_id="15813819885113216072152272732982314541699379061413472400559002281054448496477", 
    )
)
print(resp)