from decimal import Decimal
from django.http import JsonResponse
from .models import DeliveryPrice


def index(request):
    '''
    Ex: logistics/?departure=Охаdestination=Хабаровск&volume=0.61&weight=194.24
    '''
    price = 0
    error = ''

    departure = request.GET.get('departure', '')
    destination = request.GET.get('destination', '')
    weigth_str = request.GET.get('weight')

    weigth = Decimal(weigth_str)

    result = DeliveryPrice.objects.filter(
        departure=departure,
        destination=destination,
        weight_from__lte=weigth,
        weight_to__gte=weigth)

    if result.count() == 0:
        error = 'Не найден подходящий тариф'
    else:
        price_record = result[0]
        price_type = price_record.price_type.name
        base_price = price_record.base_price
        expedition_price = price_record.expedition_price
        delivery_company = price_record.delivery_company.name

        if price_type == 'Всего':
            price = base_price + expedition_price
        elif price_type == 'За 1 кг.':
            price = base_price * weigth + expedition_price
        else:
            price = 0
            error = 'Неизвестный тип тарифа'

        price = round(price, 2)

    resp = {
        'departure': departure,
        'destination': destination,
        'delivery_company': delivery_company,
        'weigth': weigth,
        'price': price,
        'error': error
    }

    return JsonResponse(resp)


def calculate(request):
    return JsonResponse('')
