from django.http import JsonResponse


def index(request):
    departure = request.GET.get('departure', '')
    destination = request.GET.get('destination', '')
    volume = request.GET.get('volume')
    weigth = request.GET.get('weight')

    resp = {
        'departure': departure,
        'destination': destination,
        'volume': volume,
        'weigth': weigth
    }
    return JsonResponse(resp)


def calculate(request):
    return JsonResponse('')
