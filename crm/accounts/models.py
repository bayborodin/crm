from django.contrib.auth.models import User
from django.db import models

from core.models import Profile
from common.models import Country, City


# Account type model
class AccountType(models.Model):
    name = models.CharField(max_length=250, db_index=True,
                            verbose_name='Наименование')
    extid = models.CharField(max_length=36, db_index=True,
                             verbose_name='Внешний код')
    description = models.CharField(
        max_length=250, verbose_name='Описание', blank=True)

    @classmethod
    def from_tuple(cls, row):
        account_type, created = AccountType.objects.get_or_create(extid=row[1])
        if created:
            res = 'Создан новый Тип Контрагента'
        else:
            res = 'Обновлен тип контрагента'

        account_type.extid = row[1]
        account_type.name = row[2]
        account_type.description = row[3]
        account_type.save()

        return res

    class Meta:
        ordering = ['name']
        verbose_name = 'Тип контрагента'
        verbose_name_plural = 'Типы контрагентов'

    def __str__(self):
        return self.name


# Account model
class Account(models.Model):
    account_type = models.ForeignKey(
        AccountType,
        related_name='accounts',
        verbose_name='Тип',
        on_delete=models.PROTECT,
        null=True,
    )
    name = models.CharField(max_length=250, db_index=True,
                            verbose_name='Наименование')
    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name='Внешний код'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, verbose_name='Ответственный', on_delete=models.PROTECT, null=True,
    )
    primary_legal_entity = models.ForeignKey(
        'LegalEntity',
        verbose_name='Основное юр. лицо',
        related_name='parent_account',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    @classmethod
    def from_tuple(cls, row):
        account, created = Account.objects.get_or_create(extid=row[1])
        if created:
            res = 'Создан новый контрагент'
        else:
            res = 'Обновлен контрагент'

        account.extid = row[1]
        account.name = row[2]

        account_types = AccountType.objects.filter(extid=row[4])
        if account_types.exists():
            account.account_type = account_types[0]

        owners = Profile.objects.filter(tsid=row[3])
        if owners.exists():
            account.owner = owners[0].user

        account.save()

        return res

    class Meta:
        ordering = ['name']
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return self.name


class LegalEntity(models.Model):
    extid = models.CharField(
        max_length=36, db_index=True, null=True, verbose_name='Внешний код'
    )
    account = models.ForeignKey(
        Account,
        related_name='legal_entities',
        verbose_name='Контрагент',
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=250, db_index=True,
                            verbose_name='Наименование')
    short_name = models.CharField(
        max_length=250, db_index=True, verbose_name='Сокращенное наименование'
    )
    inn = models.CharField(max_length=12, db_index=True, verbose_name='ИНН')
    kpp = models.CharField(
        max_length=9, db_index=True, verbose_name='КПП', null=True, blank=True
    )
    code_1c = models.CharField(
        max_length=9, db_index=True, verbose_name='Код в 1С')
    country = models.ForeignKey(
        Country,
        related_name='nation_legal_entities',
        verbose_name='Страна',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        City,
        related_name='domestic_legal_entities',
        verbose_name='Город',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    @classmethod
    def from_tuple(cls, row):
        legal_entities = LegalEntity.objects.filter(extid=row[1])
        if legal_entities.exists():
            legal_entity = legal_entities[0]
            res = 'Updated existing legal entity.'
        else:
            legal_entity = LegalEntity(extid=row[1])
            res = 'Created new legal entity'

        accounts = Account.objects.filter(extid=row[2])
        if accounts.exists():
            legal_entity.account = accounts[0]
        else:
            raise ValueError('Unknown account ID in lecal entity data.')

        countries = Country.objects.filter(extid=row[17])
        if countries.exists():
            legal_entity.country = countries[0]

        cities = City.objects.filter(extid=row[18])
        if cities.exists():
            legal_entity.city = cities[0]

        legal_entity.name = row[3]
        legal_entity.short_name = row[4]
        legal_entity.inn = row[10][:12]  # inn length is 12 symbols
        legal_entity.kpp = row[12][:9]  # kpp lenght is 9 symbols
        legal_entity.code_1c = row[16][:9]  # 1c code length is 9 symbols

        legal_entity.save()

        if row[19] == '1':
            account = legal_entity.account
            account.primary_legal_entity = legal_entity
            account.save()

        return res

    class Meta:
        ordering = ['name']
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return f'{self.short_name} (ИНН {self.inn})'
