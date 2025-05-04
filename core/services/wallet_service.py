import json

from django.http import JsonResponse

from core.models import WalletModel


class WalletService:
    def get_count(self):
        return WalletModel.objects.count()

    def create_wallet(self, request):
        try:
            print(f"Request: {request}")
            print(f"Desmadre: {request.decode('utf-8')}")
            wallet = json.loads(request)
            print(f"Desmadre: {wallet}")
        except Exception as e:
            # raise e
            return JsonResponse({
                "message": "An error occurred when loading the JSON data",
                "status_code": 400
            })

        required_fields = ["name", "amount"]
        missing_fields = [field for field in required_fields if field not in wallet]

        if missing_fields:
            return {
                "message": f"Faltan campos: {', '.join(missing_fields)}",
                "status_code": 400
            }

        try:
            wallet["amount"] = str(wallet["amount"])
            wallet_response = WalletModel.objects.create(**wallet)
        except Exception as e:
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
