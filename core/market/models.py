# from django.db import models

# # Create your models here.
# from django.db import models


# class Coin(models.Model):
#     symbol = models.CharField(
#         max_length=20,
#         unique=True,
#         db_index=True,
#     )

#     name = models.CharField(
#         max_length=100,
#     )

#     logo = models.URLField(
#         blank=True,
#         null=True,
#     )

#     is_active = models.BooleanField(
#         default=True,
#         db_index=True,
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True,
#     )

#     updated_at = models.DateTimeField(
#         auto_now=True,
#     )

#     class Meta:
#         ordering = ["symbol"]
#         verbose_name = "Coin"
#         verbose_name_plural = "Coins"

#     def __str__(self):
#         return f"{self.name} ({self.symbol})"
# import requests


# class BinanceService:
#     BASE_URL = "https://api.binance.com"

#     TIMEOUT = 5

#     @classmethod
#     def _request(cls, endpoint, params=None):
#         url = f"{cls.BASE_URL}{endpoint}"

#         response = requests.get(
#             url,
#             params=params,
#             timeout=cls.TIMEOUT,
#         )

#         response.raise_for_status()

#         return response.json()

#     # -----------------------------------------
#     # Single Price
#     # -----------------------------------------

#     @classmethod
#     def get_price(cls, symbol):
#         symbol = symbol.upper()

#         return cls._request(
#             "/api/v3/ticker/price",
#             params={
#                 "symbol": symbol,
#             },
#         )

#     # -----------------------------------------
#     # All Prices
#     # -----------------------------------------

#     @classmethod
#     def get_all_prices(cls):
#         return cls._request(
#             "/api/v3/ticker/price"
#         )

#     # -----------------------------------------
#     # 24h Ticker
#     # -----------------------------------------

#     @classmethod
#     def get_24h_ticker(cls, symbol):
#         symbol = symbol.upper()

#         return cls._request(
#             "/api/v3/ticker/24hr",
#             params={
#                 "symbol": symbol,
#             },
#         )

#     # -----------------------------------------
#     # All 24h Tickers
#     # -----------------------------------------

#     @classmethod
#     def get_all_24h_tickers(cls):
#         return cls._request(
#             "/api/v3/ticker/24hr"
#         )

#     # -----------------------------------------
#     # Klines
#     # -----------------------------------------

#     @classmethod
#     def get_klines(
#         cls,
#         symbol,
#         interval="1h",
#         limit=100,
#     ):
#         symbol = symbol.upper()

#         return cls._request(
#             "/api/v3/klines",
#             params={
#                 "symbol": symbol,
#                 "interval": interval,
#                 "limit": limit,
#             },
#         )