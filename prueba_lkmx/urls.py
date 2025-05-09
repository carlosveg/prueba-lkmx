"""
URL configuration for prueba_lkmx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.routes.auth0_routes import get_auth0_token
from core.routes.test_routes import test
from core.routes.wallets_routes import count, create_wallet

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("test/", test),
    path("wallets/count", count),
    path("wallets/create", create_wallet),
    path("auth0/token", get_auth0_token)
]
