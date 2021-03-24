from django.db import models


class contactsModel(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Введите Ваше имя')
    phone = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Введите Ваш номер телефона')
    email = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Введите Ваш Email')
    description = models.TextField(max_length=1500, null=True, blank=True, verbose_name='Опишите объект:')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['-published']


class FooterModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш телефон')
    email = models.CharField(max_length=30, db_index=True, verbose_name='Введите Ваш Email')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-published']


class OrderCalculationModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    description = models.TextField(max_length=1500, null=True, blank=True, db_index=True, verbose_name='Ремонт')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расчет стоимости косметического ремонта'
        verbose_name_plural = 'Расчеты стоимости косметического ремонта'
        ordering = ['-published']


class KapRemModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    description = models.TextField(max_length=1500, null=True, blank=True, db_index=True, verbose_name='Ремонт')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расчет стоимости капитального ремонта'
        verbose_name_plural = 'Расчеты стоимости капитального ремонта'
        ordering = ['-published']


class EuroRemModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    description = models.TextField(max_length=1500, null=True, blank=True, db_index=True, verbose_name='Ремонт')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расчет стоимости евроремонта'
        verbose_name_plural = 'Расчеты стоимости евроремонта'
        ordering = ['-published']


class DiscountModel(models.Model):
    phone = models.CharField(max_length=15, verbose_name='Ваш телефон')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Запрос на скидку'
        verbose_name_plural = 'Запросы на скидку'
        ordering = ['-published']
