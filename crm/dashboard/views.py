from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from metrics.models import Metric, WeekResult


@login_required
def index(request):
    orders_cnt_cur_week = 0  # кол-во заказов на этой неделе
    orders_sum_cur_week = 0  # сумма заказов на этой неделе

    orders_cnt_prev_week = 0  # кол-во заказов на предыдущей неделе
    orders_sum_prev_week = 0  # сумма заказов на предыдущей неделе

    today = datetime.today()
    previous_week_day = today + timedelta(days=-7)

    order_metric = Metric.objects.get(name="Заказ")

    order_statistics_current = WeekResult.objects.filter(
        metric=order_metric, year=today.year, week=today.isocalendar()[1]
    )

    order_statistics_previous = WeekResult.objects.filter(
        metric=order_metric,
        year=previous_week_day.year,
        week=previous_week_day.isocalendar()[1],
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
            (orders_cnt_cur_week - orders_cnt_prev_week) / orders_cnt_prev_week * 100
        )

    if orders_sum_prev_week == 0:
        orders_sum_percent = "__"
    else:
        orders_sum_percent = round(
            (orders_sum_cur_week - orders_sum_prev_week) / orders_sum_prev_week * 100
        )

    context = {
        "section": "dashboard",
        "orders_cnt": orders_cnt_cur_week,
        "orders_cnt_percent": orders_cnt_percent,
        "orders_sum": orders_sum_cur_week,
        "orders_sum_percent": orders_sum_percent,
    }
    return render(request, "dashboard/index.html", context)
