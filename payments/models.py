from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название квартиры")
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contract(models.Model):
    PREPAYMENT = 'Предоплата'
    CURRENTPAYMENT = 'Текущий платеж'
    POSTPAYMENT = 'Постоплата'


    TYPE_CHOICES = [
        (PREPAYMENT, 'Предоплата'),
        (CURRENTPAYMENT, 'Текущий платеж'),
        (POSTPAYMENT, 'Постоплата')
    ]

    UK = 'Управляющая компания'
    MOEK = 'МОЭК'
    MVK = 'Мосводоканал'
    MES = 'Мосэнергосбыт'
    EPD = 'ЕПД'
    NET = 'Интернет'

    PROVIDERS_CHOICES = [
        (UK, 'Управляющая компания'),
        (MOEK, 'МОЭК'),
        (MVK, 'Мосводоканал'),
        (MES, 'Мосэнергосбыт'),
        (EPD, 'ЕПД'),
        (NET, 'Интернет')
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Номер договора")
    date = models.DateField(null=False, blank=False, verbose_name="Дата договора")
    provider = models.CharField(max_length=20, choices=PROVIDERS_CHOICES, null=False, blank=False,
                                verbose_name="Поставщик услуги")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=False, blank=False,
                            verbose_name="Тип договора")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.provider} - {self.name}'


class Payment(models.Model):
    JANUARY = 'Январь'
    FEBRUARY = 'Февраль'
    MARCH = 'Март'
    APRIL = 'Апрель'
    MAY = 'Май'
    JUNE = 'Июнь'
    JULY = 'Июль'
    AUGUST = 'Август'
    SEPTEMBER = 'Сентябрь'
    OCTOBER = 'Октябрь'
    NOVEMBER = 'Ноябрь'
    DECEMBER = 'Декабрь'

    MONTH_CHOICES = [
        (JANUARY, 'Январь'),
        (FEBRUARY, 'Февраль'),
        (MARCH, 'Март'),
        (APRIL, 'Апрель'),
        (MAY, 'Май'),
        (JUNE, 'Июнь'),
        (JULY, 'Июль'),
        (AUGUST, 'Август'),
        (SEPTEMBER, 'Сентябрь'),
        (OCTOBER, 'Октябрь'),
        (NOVEMBER, 'Ноябрь'),
        (DECEMBER, 'Декабрь')
    ]

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False, verbose_name="Сумма платежа")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    period = models.CharField(max_length=20, choices=MONTH_CHOICES, null=False, blank=False,
                              verbose_name="Период оплаты")
    file = models.FileField(upload_to='payments/bills', null=True, blank=True,
                            verbose_name="Файл платежки")

    def __str__(self):
        return f'Платеж от {self.created_at.day}/{self.created_at.month}/{self.created_at.year}'