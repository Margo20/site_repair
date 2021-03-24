from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation, authenticate
from django.forms import ModelForm
from django.shortcuts import redirect

from .models import contactsModel
from django import forms


class contactsForm(ModelForm):
    name = forms.CharField(label='Введите Ваше имя', max_length=150)
    phone = forms.IntegerField(label='Введите Ваш номер телефона', widget=forms.NumberInput, help_text='только цифры(80xxxxxxxxxx)')
    email = forms.CharField(max_length=100, label='Введите Ваш Email', widget=forms.EmailInput)
    description = forms.CharField(max_length=1500, required=False,
                                  label='Опишите объект: Площадь объекта, тип объекта(Квартира, Дом, Офис, Другое.'
                                        'Тип недвижимости (Новое жилье, Вторичное жилье, Наличие дизайн-проекта', widget=forms.Textarea)

    class Meta:
        model = contactsModel
        fields = ['name', 'phone', 'email', 'description']
