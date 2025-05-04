from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from core.services.wallet_service import WalletService

wallet_service = WalletService()


@require_http_methods(["GET"])
def count(request):
    count = wallet_service.get_count()

    return JsonResponse({
        "Total de wallets": count
    })


@csrf_exempt
@require_http_methods(["POST"])
def create_wallet(request):
    print(request.body)
    wallet_response = wallet_service.create_wallet(request.body)

    return JsonResponse(wallet_response, status=wallet_response.get("status_code", 201))
