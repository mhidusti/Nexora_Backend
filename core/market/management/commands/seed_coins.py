# from django.core.management.base import BaseCommand

# from market.models import Coin


# COINS = [
#     {
#         "symbol": "BTC",
#         "name": "Bitcoin",
#     },
#     {
#         "symbol": "ETH",
#         "name": "Ethereum",
#     },
#     {
#         "symbol": "BNB",
#         "name": "BNB",
#     },
#     {
#         "symbol": "SOL",
#         "name": "Solana",
#     },
#     {
#         "symbol": "XRP",
#         "name": "XRP",
#     },
#     {
#         "symbol": "ADA",
#         "name": "Cardano",
#     },
#     {
#         "symbol": "DOGE",
#         "name": "Dogecoin",
#     },
#     {
#         "symbol": "AVAX",
#         "name": "Avalanche",
#     },
#     {
#         "symbol": "TON",
#         "name": "Toncoin",
#     },
#     {
#         "symbol": "TRX",
#         "name": "TRON",
#     },
#     {
#         "symbol": "DOT",
#         "name": "Polkadot",
#     },
#     {
#         "symbol": "LINK",
#         "name": "Chainlink",
#     },
#     {
#         "symbol": "LTC",
#         "name": "Litecoin",
#     },
#     {
#         "symbol": "SHIB",
#         "name": "Shiba Inu",
#     },
# ]


# class Command(BaseCommand):

#     help = "Seed initial Nexora coins"

#     def handle(self, *args, **options):

#         for coin_data in COINS:

#             coin, created = Coin.objects.update_or_create(
#                 symbol=coin_data["symbol"],
#                 defaults={
#                     "name": coin_data["name"],
#                     "is_active": True,
#                 },
#             )

#             if created:

#                 self.stdout.write(
#                     self.style.SUCCESS(
#                         f"Created: {coin.symbol}"
#                     )
#                 )

#             else:

#                 self.stdout.write(
#                     self.style.WARNING(
#                         f"Updated: {coin.symbol}"
#                     )
#                 )

#         self.stdout.write(
#             self.style.SUCCESS(
#                 "Coins seeded successfully."
#             )
#         )