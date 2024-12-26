
# Quick [polymarket](https://polymarket.com/) [api](https://docs.polymarket.com) setup tutorial 

This tutorial shows how to set up a Polymarket account to use its [CLOB API](https://docs.polymarket.com/#clob-api) using Python.

## Part 1 - Set Up Polymarket Account

1. Create polymarket account using non-wallet method (e.g. email). If you choose wallet method, you need to setup [allowances](https://docs.polymarket.com/#allowances).
2. Deposit funds and place one trade.
3. Export your private key (see [how to export private key](https://learn.polymarket.com/how-to-export-private-key))
4. Get the "funder" address, which is the same as USDC deposit address.

![polymarket.png](./img/polymarket.png) 

## Part 2 - Python

1. To get markets and events you can use [Gamma Markets API](https://docs.polymarket.com/#gamma-markets-api) :

```
closed = "false"
active = "true"
limit = 100
tag = "bitcoin"
markets = requests.get(f"https://gamma-api.polymarket.com/markets?tag={tag}&limit={limit}&closed={closed}&active={active}")
```
Check all the filtering and sorting available.


2. Install Requirements : `pip install -r requirements.txt`


# Create CLOB client and get/set API credentials
```
client = ClobClient(
    HOST,
    key=KEY,
    chain_id=CHAIN_ID,
    funder=FUNDER,
    signature_type=1,
)
client.set_api_creds(client.create_or_derive_api_creds())
```

4. See your current orders
```python
print(client.get_orders())
```

5. Place order

- price = we offer 0.10$ to win $1
- size = we do that 10x, so $1 to win $10
- side = BUY or SELL, imported from `py_clob_client.order_builder.constants` 
- token_id = from the markets (clobTokenIds)
```python
resp = client.create_and_post_order(
    OrderArgs(
        price=0.10,
        size=10.0,
        side=BUY,
        token_id="34731657770883441140875001518098751138877095477683682718012432921110142479972", # from events.json
    )
)
print(resp)
```

6. List orders and cancel all orders
```python
print(client.get_orders())
print("-"*25)
print(client.cancel_all())
print("-"*25)
print(client.get_orders())
```