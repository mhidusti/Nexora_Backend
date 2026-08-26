import requests


class CoinMarketCapService:
    BASE_URL = "https://pro-api.coinmarketcap.com/public-api"

    COINS = {
        "BTC": 1,
        "ETH": 1027,
    }

    @classmethod
    def get_prices(cls):
        coin_ids = ",".join(
            str(coin_id)
            for coin_id in cls.COINS.values()
        )

        response = requests.get(
            f"{cls.BASE_URL}/v1/simple/price",
            params={
                "ids": coin_ids,
                "convert": "USD",
            },
            timeout=10,
        )

        response.raise_for_status()

        result = response.json()

        markets = []

        for symbol, coin_id in cls.COINS.items():
            coin = next(
                item
                for item in result["data"]
                if item["id"] == coin_id
            )

            markets.append({
                "symbol": symbol,
                "price": coin["price"],
            })

        return markets






















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

#     # =====================================================
#     # Single Price
#     # GET /api/v3/ticker/price
#     # =====================================================

#     @classmethod
#     def get_price(cls, symbol):
#         symbol = symbol.upper()

#         return cls._request(
#             "/api/v3/ticker/price",
#             params={
#                 "symbol": symbol,
#             },
#         )

#     # =====================================================
#     # All Prices
#     # GET /api/v3/ticker/price
#     # =====================================================

#     @classmethod
#     def get_all_prices(cls):
#         return cls._request(
#             "/api/v3/ticker/price"
#         )

#     # =====================================================
#     # 24h Ticker
#     # GET /api/v3/ticker/24hr
#     # =====================================================

#     @classmethod
#     def get_24h_ticker(cls, symbol):
#         symbol = symbol.upper()

#         return cls._request(
#             "/api/v3/ticker/24hr",
#             params={
#                 "symbol": symbol,
#             },
#         )

#     # =====================================================
#     # All 24h Tickers
#     # GET /api/v3/ticker/24hr
#     # =====================================================

#     @classmethod
#     def get_all_24h_tickers(cls):
#         return cls._request(
#             "/api/v3/ticker/24hr"
#         )

#     # =====================================================
#     # Klines / Candles
#     # GET /api/v3/klines
#     # =====================================================

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