from django.apps import AppConfig


class MetricsConfig(AppConfig):
    name = 'metrics'
    verbose_name = 'Аналитика'

    def ready(self):
        import metrics.signals  # noqa
