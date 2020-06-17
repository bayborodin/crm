from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from metrics.models import Metric, WeekResult

WORK_WEEK_LENGTH = 5


def get_metrics_rate(prev_val, cur_val):
    """Compare the metrics value with the previous week"""
    week_day = datetime.today().weekday() + 1
    if week_day > WORK_WEEK_LENGTH:
        week_day = WORK_WEEK_LENGTH

    return round(
        (cur_val / week_day - prev_val / WORK_WEEK_LENGTH)
        / (prev_val / WORK_WEEK_LENGTH)
        * 100
    )


@login_required
def index(request):
    today = datetime.today()
    week_ago = today + timedelta(days=-7)

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
        orders_cnt_percent = get_metrics_rate(orders_cnt_prev_week, orders_cnt_cur_week)

    if orders_sum_prev_week == 0:
        orders_sum_percent = "__"
    else:
        orders_sum_percent = get_metrics_rate(orders_sum_prev_week, orders_sum_cur_week)

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
        shipments_cnt_percent = get_metrics_rate(
            shipments_cnt_prev_week, shipments_cnt_cur_week
        )

    if shipments_sum_prev_week == 0:
        shipments_sum_percent = "__"
    else:
        shipments_sum_percent = get_metrics_rate(
            shipments_sum_prev_week, shipments_sum_cur_week
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
        payments_cnt_percent = get_metrics_rate(
            payments_cnt_prev_week, payments_cnt_cur_week
        )

    if payments_sum_prev_week == 0:
        payments_sum_percent = "__"
    else:
        payments_sum_percent = get_metrics_rate(
            payments_sum_prev_week, payments_sum_cur_week
        )

    # МЕТРИКА - ЗВОНКИ
    calls_cnt_cur_week = 0  # кол-во звонков на этой неделе
    calls_cnt_prev_week = 0  # кол-во звонков на предыдущей неделе

    calls_metric = Metric.objects.get(name="Звонок")

    call_statistics_current = WeekResult.objects.filter(
        metric=calls_metric, year=today.year, week=today.isocalendar()[1],
    )

    call_statistics_previous = WeekResult.objects.filter(
        metric=calls_metric, year=week_ago.year, week=week_ago.isocalendar()[1],
    )

    if call_statistics_current.exists():
        calls_cnt_cur_week = call_statistics_current[0].cnt

    if call_statistics_previous.exists():
        calls_cnt_prev_week = call_statistics_previous[0].cnt

    if calls_cnt_prev_week == 0:
        calls_cnt_percent = "__"
    else:
        calls_cnt_percent = get_metrics_rate(calls_cnt_prev_week, calls_cnt_cur_week)

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
        "calls_cnt": calls_cnt_cur_week,
        "calls_cnt_percent": calls_cnt_percent,
    }

    return render(request, "dashboard/index.html", context)
