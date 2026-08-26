# from rest_framework import serializers


# class PriceSerializer(serializers.Serializer):
#     symbol = serializers.CharField()

#     price = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )


# class TickerSerializer(serializers.Serializer):
#     symbol = serializers.CharField()

#     price = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     price_change = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     price_change_percent = serializers.DecimalField(
#         max_digits=20,
#         decimal_places=8,
#     )

#     weighted_average_price = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     open_price = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     high_price = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     low_price = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     volume = serializers.DecimalField(
#         max_digits=40,
#         decimal_places=12,
#     )

#     quote_volume = serializers.DecimalField(
#         max_digits=40,
#         decimal_places=12,
#     )

#     open_time = serializers.IntegerField()

#     close_time = serializers.IntegerField()


# class CandleSerializer(serializers.Serializer):
#     open_time = serializers.IntegerField()

#     open = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     high = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     low = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     close = serializers.DecimalField(
#         max_digits=30,
#         decimal_places=12,
#     )

#     volume = serializers.DecimalField(
#         max_digits=40,
#         decimal_places=12,
#     )

#     close_time = serializers.IntegerField()