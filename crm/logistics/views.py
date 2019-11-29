from decimal import Decimal
from django.http import JsonResponse
from .models import DeliveryPrice


def index(request):
    '''
    Ex: logistics/?departure=Охаdestination=Хабаровск&volume=0.61&weight=194.24&expedition=1
    '''
    price = 0
    expedition_price = 0
    error = ''

    departure = request.GET.get('departure', '')
    destination = request.GET.get('destination', '')
    weigth_str = request.GET.get('weight')
    expedition = request.GET.get('expedition')

    weigth = Decimal(weigth_str)

    result = DeliveryPrice.objects.filter(
        departure=departure,
        destination=destination,
        weight_from__lte=weigth,
        weight_to__gte=weigth)

    if result.count() == 0:
        error = 'Не найден подходящий тариф'
        delivery_company = 'Не удалось подобрать ТК'
    else:
        price_record = result[0]
        price_type = price_record.price_type.name
        base_price = price_record.base_price
        expedition_price = price_record.expedition_price
        delivery_company = price_record.delivery_company.name

        if price_type == 'Всего':
            price = base_price + (expedition_price if expedition == '1' else 0)
        elif price_type == 'За 1 кг.':
            price = base_price * weigth + (expedition_price if expedition == '1' else 0)
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
        'include_expedition': (expedition_price if expedition == '1' else 0),
        'error': error
    }

    return JsonResponse(resp)


def calculate(request):
    return JsonResponse('')
