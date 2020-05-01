from django.db import models


class LeadChannel(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["updated"]
        verbose_name = "Канал привлечения"
        verbose_name_plural = "Каналы привлечения"

    def __str__(self):
        return self.name


class LeadSource(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name="Наименование")
    secret_key = models.CharField(
        max_length=250, db_index=True, verbose_name="Секретный ключ"
    )
    description = models.CharField(max_length=250, verbose_name="Описание", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Источник лида"
        verbose_name_plural = "Источники лидов"

    def __str__(self):
        return self.name


class Lead(models.Model):
    channel = models.ForeignKey(
        LeadChannel,
        related_name="leads",
        verbose_name="Канал",
        on_delete=models.PROTECT,
    )
    source = models.ForeignKey(
        LeadSource,
        related_name="leads",
        verbose_name="Источник",
        on_delete=models.PROTECT,
    )
    inn = models.CharField(max_length=20, verbose_name="ИНН", blank=True)
    kpp = models.CharField(max_length=20, verbose_name="КПП", blank=True)
    company_name = models.CharField(max_length=250, verbose_name="Компания", blank=True)
    city = models.CharField(max_length=250, verbose_name="Город", blank=True)
    address = models.CharField(max_length=250, verbose_name="Адрес", blank=True)
    sale_channels = models.CharField(
        max_length=250, verbose_name="Каналы продаж", blank=True
    )
    sale_regions = models.CharField(
        max_length=250, verbose_name="Регионы присутствия", blank=True
    )
    sale_points = models.CharField(
        max_length=250, verbose_name="Точки продаж", blank=True
    )
    web_address = models.CharField(
        max_length=250, verbose_name="Адрес сайта", blank=True
    )
    comment = models.CharField(max_length=250, verbose_name="Комментарий", blank=True)
    first_person = models.CharField(max_length=250, verbose_name="ЛПР", blank=True)
    first_person_position = models.CharField(
        max_length=250, verbose_name="Должность", blank=True
    )
    bank_account = models.CharField(max_length=250, verbose_name="Р/С", blank=True)
    bank_name = models.CharField(max_length=250, verbose_name="Банк", blank=True)
    bank_rcbic = models.CharField(max_length=250, verbose_name="БИК", blank=True)
    bank_corr_account = models.CharField(
        max_length=250, verbose_name="Корр. счет", blank=True
    )
    contact_person = models.CharField(
        max_length=250, verbose_name="Контактное лицо", blank=True
    )
    contact_phone = models.CharField(
        max_length=250, verbose_name="Телефон для связи", blank=True
    )
    contact_email = models.CharField(
        max_length=250, verbose_name="Email для связи", blank=True
    )
    delete_mark = models.BooleanField(verbose_name="Пометка на удаление", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]
        verbose_name = "Лид"
        verbose_name_plural = "Лиды"

    def __str__(self):
        return f"Лид {self.id} от {self.created}"
