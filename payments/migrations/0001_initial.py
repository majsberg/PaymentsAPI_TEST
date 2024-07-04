# Generated by Django 5.0.6 on 2024-06-26 18:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название квартиры')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Номер договора')),
                ('date', models.DateField(verbose_name='Дата договора')),
                ('provider', models.CharField(choices=[('orion', 'УК "Орион"'), ('moek', 'МОЭК'), ('mosvodokanal', 'Мосводоканал'), ('mosenergosbyt', 'Мосэнеросбыт'), ('epd', 'Единый платежный документ'), ('108telecom', '108Телеком')], max_length=20, verbose_name='Поставщик услуги')),
                ('type', models.CharField(choices=[('prepayment', 'Предоплата'), ('currentpayment', 'Текущий платеж'), ('postpayment', 'Постоплата')], max_length=20, verbose_name='Тип договора')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Сумма платежа')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('period', models.CharField(choices=[('January', 'Январь'), ('February', 'Февраль'), ('March', 'Март'), ('April', 'Апрель'), ('May', 'Май'), ('June', 'Июнь'), ('July', 'Июль'), ('August', 'Август'), ('September', 'Сентябрь'), ('October', 'Октябрь'), ('November', 'Ноябрь'), ('December', 'Декабрь')], max_length=20, verbose_name='Период оплаты')),
                ('file', models.FileField(blank=True, null=True, upload_to='payments/bills', verbose_name='Файл платежки')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.contract')),
            ],
        ),
    ]