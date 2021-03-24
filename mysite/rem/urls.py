from django.conf.urls import url
from django.urls import path
from .views import indexOur_work_html, indexPrice, indexReviews, indexContacts, indexServices, index, footer_form, \
     discount_form, indexOrderCalculation, indexKapRem, indexEuroRem
from . import views

app_name = 'rem'

urlpatterns = [
    path('', index, name='rem'),
    path('price/', indexPrice, name='price'),
    path('reviews/', indexReviews, name='reviews'),
    path('contacts/', indexContacts, name='contacts'),
    path('services/', indexServices, name='services'),
    path('order_calculation/', indexOrderCalculation, name='order_calculation'),
    path('kap_rem/', indexKapRem, name='kap_rem'),
    path('euro_rem/', indexEuroRem, name='euro_rem'),
    path('work_html/', indexOur_work_html, name='our_work_html'),
    path('accounts/send/', footer_form, name='footersend'),
    path('accounts/main/', discount_form, name='discount'),
   ]

