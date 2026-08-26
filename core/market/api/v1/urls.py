from django.urls import path

from .views import MarketListAPIView


app_name = "market"

urlpatterns = [
    path("", MarketListAPIView.as_view(), name="market-list"),
]
























# from django.urls import path

# from . import views


# app_name = "market"


# urlpatterns = [
#     # path(
#     #     "prices/",
#     #     views.PriceListAPIView.as_view(),
#     #     name="prices",
#     # ),

#     # path(
#     #     "prices/<str:symbol>/",
#     #     views.PriceDetailAPIView.as_view(),
#     #     name="price-detail",
#     # ),

#     # path(
#     #     "ticker/<str:symbol>/",
#     #     views.TickerDetailAPIView.as_view(),
#     #     name="ticker",
#     # ),

#     # path(
#     #     "candles/<str:symbol>/",
#     #     views.CandleAPIView.as_view(),
#     #     name="candles",
#     # ),
# ]