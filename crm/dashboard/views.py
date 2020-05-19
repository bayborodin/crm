from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from metrics.models import Metric, WeekResult


@login_required
def index(request):
    today = datetime.today()
    week_ago = today + timedelta(days=-7)
    week_day = today.weekday() + 1

    # МЕТРИКА - ЗАКАЗЫ
    orders_cnt_cur_week = 0  # кол-во заказов на этой неделе
    orders_sum_cur_week = 0  # сумма заказов на этой неделе
    orders_cnt_prev_week = 0  # кол-во заказов на предыдущей неделе
    orders_sum_prev_week = 0  # сумма заказов на предыдущей неделе

    order_metric = Metric.objects.get(name="Заказ")

    order_statistics_current = WeekResult.objects.filter(
        metric=order_metric, year=today.year, week=today.isocalendar()[1]
    )

    order_statistics_previous = WeekResult.objects.filter(
        metric=order_metric, year=week_ago.year, week=week_ago.isocalendar()[1],
    )

    if order_statistics_current.exists():
        orders_cnt_cur_week = order_statistics_current[0].cnt
        orders_sum_cur_week = order_statistics_current[0].val

    if order_statistics_previous.exists():
        orders_cnt_prev_week = order_statistics_previous[0].cnt
        orders_sum_prev_week = order_statistics_previous[0].val

    if orders_cnt_prev_week == 0:
        orders_cnt_percent = "__"
    else:
        orders_cnt_percent = round(
            (orders_cnt_cur_week / week_day - orders_cnt_prev_week / 7)
            / (orders_cnt_prev_week / 7)
            * 100
        )

    if orders_sum_prev_week == 0:
        orders_sum_percent = "__"
    else:
        orders_sum_percent = round(
            (orders_sum_cur_week / week_day - orders_sum_prev_week / 7)
            / (orders_sum_prev_week / 7)
            * 100
        )

    # МЕТРИКА - ОТГРУЗКИ
    shipments_cnt_cur_week = 0  # кол-во отгрузок на этой неделе
    shipments_sum_cur_week = 0  # сумма отгрузок на этой неделе
    shipments_cnt_prev_week = 0  # кол-во отгрузок на предыдущей неделе
    shipments_sum_prev_week = 0  # сумма отгрузок на предыдущей неделе

    shipment_metric = Metric.objects.get(name="Отгрузка")

    shipment_statistics_current = WeekResult.objects.filter(
        metric=shipment_metric, year=today.year, week=today.isocalendar()[1]
    )

    shipment_statistics_previous = WeekResult.objects.filter(
        metric=shipment_metric, year=week_ago.year, week=week_ago.isocalendar()[1],
    )

    if shipment_statistics_current.exists():
        shipments_cnt_cur_week = shipment_statistics_current[0].cnt
        shipments_sum_cur_week = shipment_statistics_current[0].val

    if shipment_statistics_previous.exists():
        shipments_cnt_prev_week = shipment_statistics_previous[0].cnt
        shipments_sum_prev_week = shipment_statistics_previous[0].val

    if shipments_cnt_prev_week == 0:
        shipments_cnt_percent = "__"
    else:
        shipments_cnt_percent = round(
            (shipments_cnt_cur_week / week_day - shipments_cnt_prev_week / 7)
            / (shipments_cnt_prev_week / 7)
            * 100
        )

    if shipments_sum_prev_week == 0:
        shipments_sum_percent = "__"
    else:
        shipments_sum_percent = round(
            (shipments_sum_cur_week / week_day - shipments_sum_prev_week / 7)
            / (shipments_sum_prev_week / 7)
            * 100
        )

    # МЕТРИКА - ПЛАТЕЖИ
    payments_cnt_cur_week = 0  # кол-во оплат на этой неделе
    payments_sum_cur_week = 0  # сумма оплат на этой неделе
    payments_cnt_prev_week = 0  # кол-во оплат на предыдущей неделе
    payments_sum_prev_week = 0  # сумма оплат на предыдущей неделе

    payment_metric = Metric.objects.get(name="Поступление ДС")

    payment_statistics_current = WeekResult.objects.filter(
        metric=payment_metric, year=today.year, week=today.isocalendar()[1],
    )

    payment_statistics_previous = WeekResult.objects.filter(
        metric=payment_metric, year=week_ago.year, week=week_ago.isocalendar()[1],
    )

    if payment_statistics_current.exists():
        payments_cnt_cur_week = payment_statistics_current[0].cnt
        payments_sum_cur_week = payment_statistics_current[0].val

    if payment_statistics_previous.exists():
        payments_cnt_prev_week = payment_statistics_previous[0].cnt
        payments_sum_prev_week = payment_statistics_previous[0].val

    if payments_cnt_prev_week == 0:
        payments_cnt_percent = "__"
    else:
        payments_cnt_percent = round(
            (payments_cnt_cur_week / week_day - payments_cnt_prev_week / 7)
            / (payments_cnt_prev_week / 7)
            * 100
        )

    if payments_sum_prev_week == 0:
        payments_sum_percent = "__"
    else:
        payments_sum_percent = round(
            (payments_sum_cur_week / week_day - payments_sum_prev_week / 7)
            / (payments_sum_prev_week / 7)
            * 100
        )

    # КОНТЕКСТ
    context = {
        "section": "dashboard",
        "orders_cnt": orders_cnt_cur_week,
        "orders_cnt_percent": orders_cnt_percent,
        "orders_sum": orders_sum_cur_week,
        "orders_sum_percent": orders_sum_percent,
        "shipments_cnt": shipments_cnt_cur_week,
        "shipments_cnt_percent": shipments_cnt_percent,
        "shipments_sum": shipments_sum_cur_week,
        "shipments_sum_percent": shipments_sum_percent,
        "payments_cnt": payments_cnt_cur_week,
        "payments_cnt_percent": payments_cnt_percent,
        "payments_sum": payments_sum_cur_week,
        "payments_sum_percent": payments_sum_percent,
    }

    return render(request, "dashboard/index.html", context)
