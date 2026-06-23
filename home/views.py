from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# views.py

products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Premium sound quality with noise cancellation.",
        "image": "/static/headphone.webp"
    },
    {
        "name": "Smart Watch",
        "price": 4499,
        "description": "Track fitness, heart rate, and notifications.",
        "image": "/static/smartwatch.webp"
    },
    {
        "name": "Gaming Mouse",
        "price": 1299,
        "description": "RGB lighting with high-precision sensor.",
        "image": "/static/gamingmoues.jpg"
    },
    {
        "name": "Bluetooth Speaker",
        "price": 1999,
        "description": "Portable speaker with deep bass sound.",
        "image": "/static/bluetoothspekar.webp"
    },
    {
        "name": "Laptop Backpack",
        "price": 899,
        "description": "Water-resistant backpack with USB charging port.",
        "image": "/static/laptopbackpack.avif"
    },
    {
        "name": "Wireless Keyboard",
        "price": 1499,
        "description": "Slim design with long battery life.",
        "image": "/static/keyboard.webp"
    }
]

# Create your views here.

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def services(request):
    return render(request , 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,subject=subject,desc=desc , date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
        
    return render(request , 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def search(request):
    query = request.GET.get('q', '')

    results = []

    for product in products:
        if query.lower() in product['name'].lower():
            results.append(product)

    return render(request, 'search.html', {
        'query': query,
        'results': results
    })