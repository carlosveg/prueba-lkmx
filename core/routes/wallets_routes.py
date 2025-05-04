import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from core.auth0.auth0 import require_auth0_token
from core.services.wallet_service import WalletService

wallet_service = WalletService()

log = logging.getLogger(__name__)

@require_http_methods(["GET"])
def count(request):
    log.info("Inicia obtención de total de wallets")
    count = wallet_service.get_count()

    return JsonResponse({
        "Total de wallets": count
    })


@csrf_exempt
@require_http_methods(["POST"])
@require_auth0_token
def create_wallet(request):
    log.info("Inicia creación de wallet")
    wallet_response = wallet_service.create_wallet(request.body)

    return JsonResponse(wallet_response, status=wallet_response.get("status_code", 201))
