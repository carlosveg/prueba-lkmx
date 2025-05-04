import logging

import requests
from django.http import JsonResponse

from prueba_lkmx.environments import AUTH0_DOMAIN, AUTH0_API_IDENTIFIER, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET

log = logging.getLogger(__name__)

class Auth0Service:
    def get_token(self):
        url = f'{AUTH0_DOMAIN}/oauth/token'
        payload = {
            "client_id": AUTH0_CLIENT_ID,
            "client_secret": AUTH0_CLIENT_SECRET,
            "audience": AUTH0_API_IDENTIFIER,
            "grant_type": "client_credentials"
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if "access_token" not in data:
            log.error(f"Error al obtener token: {data}")
            # raise Exception(f"Error al obtener token: {data}")
            return JsonResponse(
                {"message": f"Error al obtener token: {data}"},
                status=500
            )

        return data["access_token"]