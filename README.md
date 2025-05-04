# Django + Auth0 + PostgreSQL API

API básica en Django con uso de tokens de auth0.

---

## Requisitos

- Python 3.8+
- PostgreSQL 14+
- Registrarse en [Auth0](https://auth0.com)

## Estructura del Proyecto

```
LKMX-test/
├── prueba_lkmx/
│   ├── __init__.py
│   ├── asgi.py
│   ├── environments.py # En este archivo se encuentran las variables de entorno ya cargadas en el proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── auth0/
│   │   └── auth0.py
│   ├── migrations/
│   │   └── __init__.py
│   │   └── 0001_initial.py
│   │   └── 0002_alter_walletmodel_id.py
│   ├── routes/
│   │   └── __init__.py
│   │   └── test_routes.py
│   │   └── wallets_routes.py
│   ├── services/
│   │   └── __init__.py
│   │   └── wallet_service.py
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── auth0.py
├── .env
├── .env.example
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
```

## Instalación

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env  # o configura manualmente tu archivo .env

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecutar el servidor local
python manage.py runserver
```

## Configuración de Auth0

1. Crea una cuenta en [Auth0](https://auth0.com).
2. Crea una aplicación (Regular Web Applications).
3. Copia el **Domain** y el **Identifier (audience)**.
4. Configurar el archivo `.env` con los valores:

```env
AUTH0_DOMAIN=
AUTH0_API_IDENTIFIER=
AUTH0_ALGORITHMS=
```

## Variables de Entorno

El archivo `.env` debe tener el siguiente contenido:

| Variable             | Descripción                                                           |
|----------------------|-----------------------------------------------------------------------|
| DB_NAME              | Nombre de la base de datos                                            |
| DB_USER              | Nombre del usuario de BD                                              |
| DB_PASSWORD          | Contraseña del usuario de BD                                          |
| DB_HOST              | Host de la BD                                                         |
| DB_PORT              | Puerto donde corre el demonio de postgres                             |
| AUTH0_DOMAIN         | Dominio que se ortorga al crear la App en [Auth0](https://auth0.com). |
| AUTH0_API_IDENTIFIER | Identificador de la api creada en [Auth0](https://auth0.com).         |
| AUTH0_ALGORITHMS     | Algoritmo del token auth0                                             |

## Endpoints Disponibles

- `GET /test/` — Revisar si el servidor ya se encuentra disponible
- `POST /wallets/create` — Crear un wallet (requiere token JWT).
- `GET /wallets/count` — Contar los wallets registrados.
- `GET /auth0/token` — Obtener token de auth0 # requiere header 'X-API-Key'

## Ejemplo de uso con curl

> [!IMPORTANT]
> Para obtener el token de auth0 actualmente es necesario usar cURL para obtenerlo (el snippet se los compartiré como
> archivo adjunto)
> Se agregó un endpoint que requiere una api key para poder consumirlo, este endpoint devuelve el token de oauth para
> poder consumir el endpoint de creación de wallet

```bash
# Obtener un token desde Auth0 (usando client credentials o dashboard)

# Crear wallet (requiere Authorization: Bearer <token>)
curl --location 'http://localhost:8000/wallets/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <TOKEN>' \
--data '{
	"name": "Apartado 2",
	"amount": 14
}'

```

```bash
# Consultar total de libros registrados
curl --location 'http://localhost:8000/wallets/count'
```

```bash
# Consultar estado del servicio
curl --location 'http://localhost:8000/test'
```

```bash
# Obtener token auth0
curl --location 'http://localhost:8000/auth0/token' \
--header 'x-api-key: <API KEY>'
```

## Logger

Puedes agregar tus propios logs usando el sistema de logging de Django. Se ha configurado para mostrar mensajes de nivel
`INFO` y superior en consola.

Ejemplo de uso en cualquier vista o servicio:

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Mensaje informativo personalizado")
```

## Notas Finales

- Los modelos se declaran en `core/models.py`.
- Los endpoints se definen en `core/routes/` y se exponen vía `prueba_lkmx/urls.py`.
- Se usa Auth0 para la validación de tokens JWT usando la librería `python-jose`.
- Puedes extender el proyecto fácilmente agregando más modelos, servicios y endpoints.