from django.shortcuts import render, redirect
from .forms import contactsForm
from .models import FooterModel, contactsModel, DiscountModel, OrderCalculationModel, KapRemModel, EuroRemModel


def footer_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        record = FooterModel.objects.create(name=name, phone=phone, email=email)
        message ='Ваша заявка отправлена'
        return render(request, template_name='pages/main.html', context={'message': message})
    else:
        return render(request, template_name='pages/main.html')


def discount_form(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        record = DiscountModel.objects.create(phone=phone)
        message ='Благодарим за информацию'
        return render(request, template_name='pages/main.html', context={'message': message})
    else:
        return render(request, template_name='pages/main.html')


def index(request):
    data = request.POST
    return render(request, 'pages/main.html')


def indexOur_work_html(request):
    return render(request, 'pages/our_work.html')


def indexPrice(request):
    return render(request, 'pages/price.html')


def indexContacts(request):
    data = request.POST
    dataDBUser = contactsModel.objects.all()
    if request.POST:
        form = contactsForm(request.POST)
        phone = data['phone']
        if len(phone) < 9:
            return render(request, 'pages/base.html', {'error': 'Номер телефона должен содержать не менее 11 символов', 'color': 'red'})
        else:
            form.save()
            return render(request, 'pages/base.html', {'success': 'Благодарим за информацию!', 'color': 'green'})
        return redirect('rem:rem')
    else:
        form = contactsForm()
        context = {'form': form}
        return render(request, 'pages/contacts.html', context)

    return render(request, 'pages/contacts.html', {'dataDBUser': dataDBUser})


def indexReviews(request):
    return render(request, 'pages/about_us.html')


def indexServices(request):
    return render(request, 'pages/services.html')


def indexOrderCalculation(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        record = OrderCalculationModel.objects.create(name=name, phone=phone, description=description)
        message ='Спасибо за информацию. Мы вам перезвоним'
        return render(request, template_name='pages/order_calculation.html', context={'message': message})
    else:
        return render(request, template_name='pages/order_calculation.html')


def indexKapRem(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        record = KapRemModel.objects.create(name=name, phone=phone, description=description)
        message ='Спасибо за информацию. Мы вам перезвоним'
        return render(request, template_name='pages/kap_rem.html', context={'message': message})
    else:
        return render(request, template_name='pages/kap_rem.html')


def indexEuroRem(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        record = EuroRemModel.objects.create(name=name, phone=phone, description=description)
        message ='Спасибо за информацию. Мы вам перезвоним'
        return render(request, template_name='pages/euro_rem.html', context={'message': message})
    else:
        return render(request, template_name='pages/euro_rem.html')
