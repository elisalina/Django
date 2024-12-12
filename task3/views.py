from django.shortcuts import render

def laundry(request):
    return render(request, 'third_task/laundry.html')

def services(request):
    services = {
        'first': 'Постирать',
        'second': 'Посушить',
        'third': 'Погладить'
    }
    return render(request, 'third_task/catalog.html', context=services)

def cart(request):
    return render(request, 'third_task/cart.html')


# Create your views here.
