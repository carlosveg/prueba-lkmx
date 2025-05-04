import requests
from django.http import JsonResponse
from jose import jwt

from prueba_lkmx.environments import AUTH0_DOMAIN, AUTH0_ALGORITHMS, AUTH0_API_IDENTIFIER

import logging

log = logging.getLogger(__name__)

def get_auth_header(request):
    auth = request.headers.get('Authorization', None)

    if not auth:
        return None

    parts = auth.split()

    if parts[0].lower() != 'bearer' or len(parts) != 2:
        return None

    return parts[1]


def require_auth0_token(func):
    def wrapper(request, *args, **kwargs):
        token = get_auth_header(request)

        if not token:
            log.error("Auth header is missing")
            return JsonResponse({
                "message": "Auth header is missing"
            }, status=401)

        try:
            jsonurl = requests.get(f"{AUTH0_DOMAIN}/.well-known/jwks.json")
            jwks = jsonurl.json()
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = None

            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }

            if rsa_key:
                try:
                    payload = jwt.decode(
                        token,
                        rsa_key,
                        algorithms=AUTH0_ALGORITHMS,
                        audience=AUTH0_API_IDENTIFIER,
                        issuer=f"{AUTH0_DOMAIN}/"
                    )
                except Exception as e:
                    log.error(f"An error occurred while decoding the token: {e}")
                    return JsonResponse({
                        "message": f"An error occurred while decoding the token: {e}"
                    }, status=401)
            else:
                log.error("Invalid header")
                return JsonResponse({
                    "message": "Invalid header"
                }, status=401)
        except Exception as e:
            log.error(f"An error occurred while validating the token: {e}")
            return JsonResponse({
                "message": f"An error occurred while validating the token: {e}"
            })

        return func(request, *args, **kwargs)
    return wrapper