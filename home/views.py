from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
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
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('/register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('/register')

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully!")
        return redirect('/login')

    return render(request, 'register.html')

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        print("Authenticated User:", user)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid Username or Password!")

        
    
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

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