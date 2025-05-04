from django.http import JsonResponse

from core.models import WalletModel


def count(request):
    count = WalletModel.objects.count()

    return JsonResponse({
        "count": count
    })