from django.db import models


# Communication type model
class CommunicationType(models.Model):
    extid = models.CharField(max_length=36, db_index=True, blank=True)
    name = models.CharField(max_length=250, verbose_name="Наименование")
    code = models.CharField(max_length=6, verbose_name="Код")
    is_phone = models.BooleanField(default=False, verbose_name="Для звонков")

    @classmethod
    def from_tuple(cls, row):
        communication_type, created = CommunicationType.objects.get_or_create(
            extid=row[1]
        )
        if created:
            res = "Создан новый Тип Контрагента"
        else:
            res = "Обновлен тип контрагента"

        communication_type.extid = row[1]
        communication_type.name = row[2]
        communication_type.code = row[3]
        communication_type.is_phone = row[4] == "1"
        communication_type.save()

        return res

    class Meta:
        ordering = ["name"]
        verbose_name = "Тип средства связи"
        verbose_name_plural = "Типы средств связи"

    def __str__(self):
        return self.name


# Country model
class Country(models.Model):
    extid = models.CharField(max_length=36, db_index=True, blank=True)
    name = models.CharField(max_length=250, verbose_name="Наименование")

    @classmethod
    def from_tuple(cls, row):
        country, created = Country.objects.get_or_create(extid=row[1])
        if created:
            res = "Создана новая страна"
        else:
            res = "Обновлена страна"

        country.extid = row[1]
        country.name = row[2]
        country.save()

        return res

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


# State model
class State(models.Model):
    extid = models.CharField(max_length=36, db_index=True, blank=True)
    name = models.CharField(max_length=250, verbose_name='Наименование')
    country = models.ForeignKey(
        Country,
        related_name='states',
        verbose_name='Страна',
        on_delete=models.PROTECT,
        null=True,
    )

    @classmethod
    def from_tuple(cls, row):
        state, created = State.objects.get_or_create(extid=row[1])
        if created:
            res = 'Created a new state'
        else:
            res = 'Updated an existed state'

        state.extid = row[1]
        state.name = row[2]

        countries = Country.objects.filter(extid=row[3])
        if countries.exists():
            state.country = countries[0]
        else:
            raise ValueError('Unknown country ID in the state data.')

        state.save()

        return res

    class Meta(object):
        ordering = ['name']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


# City model
class City(models.Model):
    extid = models.CharField(max_length=36, db_index=True, blank=True)
    name = models.CharField(max_length=250, verbose_name='Наименование')
    country = models.ForeignKey(
        Country,
        related_name='cities',
        verbose_name='Страна',
        on_delete=models.PROTECT,
        null=True,
    )
    state = models.ForeignKey(
        State,
        related_name='subjects',
        verbose_name='Регион',
        on_delete=models.PROTECT,
        null=True,
    )
    phone_code = models.CharField(
        max_length=5, null=True, verbose_name='Тел. код')
    kladr_code = models.CharField(
        max_length=13, null=True, verbose_name='КЛАДР')

    class Meta:
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    @classmethod
    def from_tuple(cls, row):
        city, created = City.objects.get_or_create(extid=row[1])
        if created:
            res = 'Created a new city'
        else:
            res = 'Updated an existed city'

        city.extid = row[1]
        city.name = row[2]

        countries = Country.objects.filter(extid=row[3])
        if countries.exists():
            city.country = countries[0]
        else:
            raise ValueError('Unknown country ID in the city data.')

        states = State.objects.filter(extid=row[4])
        if states.exists():
            city.state = states[0]
        else:
            raise ValueError('Unknown state ID in the city data.')

        if row[5]:
            phone_code = row[5] if len(row[5]) <= 5 else row[5][:5]
            city.phone_code = phone_code

        if row[6]:
            city.kladr_code = row[6]

        city.save()

        return res
