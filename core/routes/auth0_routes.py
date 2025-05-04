from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from core.services.auth0_service import Auth0Service
from prueba_lkmx.environments import X_API_KEY

auth0_service = Auth0Service()

@require_http_methods(["GET"])
def get_auth0_token(request):
    api_key_header = request.headers.get("X-API-Key")

    if api_key_header is None or api_key_header != X_API_KEY:
        return JsonResponse({
            "message": "Header api key is missing or invalid"
        }, status=401)

    token = auth0_service.get_token()

    return JsonResponse({
        "token": token,
    })