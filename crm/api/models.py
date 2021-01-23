from django.db import models


class Integration(models.Model):
    code = models.CharField(
        max_length=2, verbose_name="Код", unique=True, db_index=True
    )
    name = models.CharField(max_length=50, verbose_name="Внешняя система")
    description = models.CharField(
        max_length=250, verbose_name="Описание", blank=True, null=True
    )

    class Meta:
        ordering = ("code",)
        verbose_name = "Интеграция"
        verbose_name_plural = "Интеграции"

    def __str__(self):
        return f"{self.name} ({self.code})"
