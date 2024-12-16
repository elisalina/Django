from django.shortcuts import render
def laundry(request):
    return render(request, 'fourth_task/laundry.html')

def services(request):
    services = [
        'Постирать',
         'Посушить',
         'Погладить'
    ]
    return render(request, 'fourth_task/catalog.html', {'services': services})

def cart(request):
    cart_info = "Ваша корзина пуста."
    return render(request, 'fourth_task/cart.html', {'cart_info': cart_info})

def base(request):
    return render(request, 'fourth_task/menu.html')

# Create your views here.
