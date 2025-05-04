from django.http import JsonResponse


def test(request):
    return JsonResponse({
        "message": "App is up and running!"
    })