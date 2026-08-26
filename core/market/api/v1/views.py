from rest_framework.response import Response
from rest_framework.views import APIView

from .services import CoinMarketCapService


class MarketListAPIView(APIView):

    def get(self, request):
        markets = CoinMarketCapService.get_prices()

        return Response({
            "data": markets
        })



















# from decimal import Decimal

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .services import CoinMarketCapService

# from .serializers import (
#     PriceSerializer,
#     TickerSerializer,
#     CandleSerializer,
# )


# # =========================================================
# # PRICE LIST
# # GET /api/v1/market/prices/
# # =========================================================

# class PriceListAPIView(APIView):
#     """
#     Get current prices of all trading pairs.
#     """

#     def get(self, request):

#         try:

#             data = CoinMarketCapService.get_all_prices()

#             result = []

#             for item in data:

#                 result.append({
#                     "symbol": item["symbol"],
#                     "price": Decimal(item["price"]),
#                 })

#             serializer = PriceSerializer(
#                 data=result,
#                 many=True,
#             )

#             serializer.is_valid(
#                 raise_exception=True
#             )

#             return Response({
#                 "success": True,
#                 "count": len(result),
#                 "data": serializer.validated_data,
#             })

#         except Exception as exc:

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         "Unable to fetch "
#                         "market prices."
#                     ),
#                     "error": str(exc),
#                 },
#                 status=status.HTTP_503_SERVICE_UNAVAILABLE,
#             )


# # =========================================================
# # SINGLE PRICE
# # GET /api/v1/market/prices/BTCUSDT/
# # =========================================================

# class PriceDetailAPIView(APIView):
#     """
#     Get current price of a specific trading pair.
#     """

#     def get(self, request, symbol):

#         try:

#             data = CoinMarketCapService.get_price(
#                 symbol
#             )

#             result = {
#                 "symbol": data["symbol"],
#                 "price": Decimal(
#                     data["price"]
#                 ),
#             }

#             serializer = PriceSerializer(
#                 data=result
#             )

#             serializer.is_valid(
#                 raise_exception=True
#             )

#             return Response({
#                 "success": True,
#                 "data": serializer.validated_data,
#             })

#         except Exception as exc:

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         f"Unable to fetch "
#                         f"price for {symbol}."
#                     ),
#                     "error": str(exc),
#                 },
#                 status=status.HTTP_503_SERVICE_UNAVAILABLE,
#             )


# # =========================================================
# # 24H TICKER
# # GET /api/v1/market/ticker/BTCUSDT/
# # =========================================================

# class TickerDetailAPIView(APIView):
#     """
#     Get 24-hour market statistics.
#     """

#     def get(self, request, symbol):

#         try:

#             data = CoinMarketCapService.get_24h_ticker(
#                 symbol
#             )

#             result = {
#                 "symbol": data["symbol"],

#                 "price": Decimal(
#                     data["lastPrice"]
#                 ),

#                 "price_change": Decimal(
#                     data["priceChange"]
#                 ),

#                 "price_change_percent": Decimal(
#                     data["priceChangePercent"]
#                 ),

#                 "weighted_average_price": Decimal(
#                     data["weightedAvgPrice"]
#                 ),

#                 "open_price": Decimal(
#                     data["openPrice"]
#                 ),

#                 "high_price": Decimal(
#                     data["highPrice"]
#                 ),

#                 "low_price": Decimal(
#                     data["lowPrice"]
#                 ),
#                 "volume": Decimal(
#                     data["volume"]
#                 ),

#                 "quote_volume": Decimal(
#                     data["quoteVolume"]
#                 ),

#                 "open_time": data["openTime"],

#                 "close_time": data["closeTime"],
#             }

#             serializer = TickerSerializer(
#                 data=result
#             )

#             serializer.is_valid(
#                 raise_exception=True
#             )

#             return Response({
#                 "success": True,
#                 "data": serializer.validated_data,
#             })

#         except Exception as exc:

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         f"Unable to fetch "
#                         f"ticker for {symbol}."
#                     ),
#                     "error": str(exc),
#                 },
#                 status=status.HTTP_503_SERVICE_UNAVAILABLE,
#             )


# # =========================================================
# # CANDLES / KLINES
# # GET /api/v1/market/candles/BTCUSDT/
# # =========================================================

# class CandleAPIView(APIView):
#     """
#     Get OHLCV candle data.

#     Example:

#     /api/v1/market/candles/BTCUSDT/?interval=1h&limit=100
#     """

#     ALLOWED_INTERVALS = {
#         "1m",
#         "3m",
#         "5m",
#         "15m",
#         "30m",
#         "1h",
#         "2h",
#         "4h",
#         "6h",
#         "8h",
#         "12h",
#         "1d",
#         "3d",
#         "1w",
#         "1M",
#     }

#     def get(self, request, symbol):

#         # -------------------------------------------------
#         # Interval
#         # -------------------------------------------------

#         interval = request.query_params.get(
#             "interval",
#             "1h",
#         )

#         if interval not in self.ALLOWED_INTERVALS:

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         "Invalid interval."
#                     ),
#                     "allowed_intervals": sorted(
#                         self.ALLOWED_INTERVALS
#                     ),
#                 },
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # -------------------------------------------------
#         # Limit
#         # -------------------------------------------------

#         limit = request.query_params.get(
#             "limit",
#             "100",
#         )

#         try:

#             limit = int(limit)

#         except (TypeError, ValueError):

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         "Limit must be an integer."
#                     ),
#                 },
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # Binance max limit = 1000
#         if limit < 1 or limit > 1000:

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         "Limit must be between "
#                         "1 and 1000."
#                     ),
#                 },
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # -------------------------------------------------
#         # Binance Request
#         # -------------------------------------------------

#         try:

#             data = CoinMarketCapService.get_klines(
#                 symbol=symbol,
#                 interval=interval,
#                 limit=limit,
#             )

#             result = []

#             for candle in data:

#                 result.append({
#                     "open_time": candle[0],

#                     "open": Decimal(
#                         candle[1]
#                     ),

#                     "high": Decimal(
#                         candle[2]
#                     ),

#                     "low": Decimal(
#                         candle[3]
#                     ),

#                     "close": Decimal(
#                         candle[4]
#                     ),
#                     "volume": Decimal(
#                         candle[5]
#                     ),

#                     "close_time": candle[6],
#                 })

#             # -------------------------------------------------
#             # Serializer
#             # -------------------------------------------------

#             serializer = CandleSerializer(
#                 data=result,
#                 many=True,
#             )

#             serializer.is_valid(
#                 raise_exception=True
#             )

#             return Response({
#                 "success": True,

#                 "symbol": symbol.upper(),

#                 "interval": interval,

#                 "count": len(result),

#                 "data": serializer.validated_data,
#             })

#         except Exception as exc:

#             return Response(
#                 {
#                     "success": False,
#                     "message": (
#                         "Unable to fetch "
#                         "candle data."
#                     ),
#                     "error": str(exc),
#                 },
#                 status=status.HTTP_503_SERVICE_UNAVAILABLE,
#             )