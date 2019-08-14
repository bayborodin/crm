from django.db import models


# Account type model
class AccountType(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Наименование')

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

    class Meta:
        ordering = ['name']
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return self.name
