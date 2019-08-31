from django.db import models


# Account type model
class AccountType(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Наименование')
    tsid = models.CharField(max_length=36, db_index=True, verbose_name='Внешний код')
    description = models.CharField(max_length=250, verbose_name='Описание', blank=True)

    @classmethod
    def from_tuple(cls, row):
        account_type, created = AccountType.objects.get_or_create(tsid=row[1])
        if created:
            res = 'Создан новый Тип Контрагента'
        else:
            res = 'Обновлен тип контрагента'

        account_type.tsid = row[1]
        account_type.name = row[2]
        account_type.description = row[3]
        account_type.save()

        return res

    class Meta:
        ordering = ['name']
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


# Account model
class Account(models.Model):
    account_type = models.ForeignKey(AccountType, related_name='accounts', verbose_name='Тип',
                                     on_delete=models.PROTECT)
    name = models.CharField(max_length=250, db_index=True, verbose_name='Наименование')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def from_tuple(cls, row):
        raise NotImplementedError

    class Meta:
        ordering = ['name']
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return self.name
