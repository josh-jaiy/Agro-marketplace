# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Transaction, Buyer, Seller
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, SellerProfileForm, BuyerProfileForm, SellerForm
from django.contrib.auth import login

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'marketplace/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product})

@login_required
def buy_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    buyer = get_object_or_404(Buyer, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if quantity > product.quantity:
            return render(request, 'marketplace/product_detail.html', {
                'product': product,
                'error_message': 'Not enough quantity available.'
            })
        total_price = quantity * product.price
        transaction = Transaction.objects.create(
            product=product,
            buyer=buyer,
            quantity=quantity,
            total_price=total_price
        )
        product.quantity -= quantity
        if product.quantity == 0:
            product.available = False
        product.save()
        return redirect('transaction_detail', pk=transaction.pk)
    return render(request, 'marketplace/buy_product.html', {'product': product})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'marketplace/transaction_detail.html', {'transaction': transaction})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_seller:
                Seller.objects.create(user=user)
            if user.is_buyer:
                Buyer.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'marketplace/register.html', {'form': form})

@login_required
def seller_profile(request):
    if request.method == 'POST':
        form = SellerProfileForm(request.POST, instance=request.user.seller)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = SellerProfileForm(instance=request.user.seller)
    return render(request, 'marketplace/seller_profile.html', {'form': form})

@login_required
def buyer_profile(request):
    if request.method == 'POST':
        form = BuyerProfileForm(request.POST, instance=request.user.buyer)
        if form.is_valid():
            form.save()
            return redirect('buyer_dashboard')
    else:
        form = BuyerProfileForm(instance=request.user.buyer)
    return render(request, 'marketplace/buyer_profile.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_seller:
        return redirect('seller_dashboard')
    elif request.user.is_buyer:
        return redirect('buyer_dashboard')
    else:
        return redirect('login')

@login_required
def seller_dashboard(request):
    if not request.user.is_seller:
        return redirect('dashboard')
    return render(request, 'marketplace/seller_dashboard.html')

@login_required
def buyer_dashboard(request):
    if not request.user.is_buyer:
        return redirect('dashboard')
    return render(request, 'marketplace/buyer_dashboard.html')

@login_required
def create_seller_profile(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            return redirect('seller_profile')  # Change to your actual profile URL
    else:
        form = SellerForm()
    return render(request, 'marketplace/create_seller_profile.html', {'form': form})


@login_required
def seller_profile(request):
    try:
        seller = request.user.seller
    except Seller.DoesNotExist:
        return redirect('create_seller_profile')
    if request.method == 'POST':
        form = SellerProfileForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = SellerProfileForm(instance=seller)
    return render(request, 'marketplace/seller_profile.html', {'form': form})

def get_started(request):
    return render(request, 'marketplace/get_started.html')



def logged_out_view(request):
   
    return redirect('/')