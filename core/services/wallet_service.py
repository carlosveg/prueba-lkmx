import json

from django.http import JsonResponse

from core.models import WalletModel

import logging

log = logging.getLogger(__name__)

class WalletService:
    def get_count(self):
        return WalletModel.objects.count()

    def create_wallet(self, request):
        try:
            wallet = json.loads(request)
        except Exception as e:
            log.error(f"An error occurred when loading the JSON data: {e}")
            # raise e
            return JsonResponse({
                "message": "An error occurred when loading the JSON data",
                "status_code": 400
            })

        required_fields = ["name", "amount"]
        missing_fields = [field for field in required_fields if field not in wallet]

        if missing_fields:
            log.error(f"Missing fields: {', '.join(missing_fields)}")
            return {
                "message": f"Missing fields: {', '.join(missing_fields)}",
                "status_code": 400
            }

        try:
            wallet["amount"] = str(wallet["amount"])
            wallet_response = WalletModel.objects.create(**wallet)
        except Exception as e:
            log.error(f"An error occurred when creating the wallet: {e}")
            # raise e
            return {
                "message": f"An error occurred when creating the wallet: {e}",
                "status_code": 500
            }

        return {
            "wallet": {
                "id": wallet_response.id,
                "name": wallet_response.name,
                "amount": wallet_response.amount
            },
            "status_code": 201,
            "message": "Wallet created successfully"
        }
