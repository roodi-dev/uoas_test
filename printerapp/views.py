from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, QuotationRequest
from django.views.decorators.http import require_POST
from django.db.models import F, Sum
from django.core.mail import send_mail

# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@require_POST
def add_to_quote(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key or request.session.save() or request.session.session_key
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    quantity = int(request.POST.get('quantity', 1))
    notes = request.POST.get('notes', '').strip()
    QuotationRequest.objects.create(
        product=product,
        user=request.user if request.user.is_authenticated else None,
        session_key=None if request.user.is_authenticated else session_key,
        quantity=quantity,
        email=email,
        notes=notes
    )
    # Send notification to admin
    send_mail(
        'New Quotation Request',
        f'Product: {product.name}\nQuantity: {quantity}\nName: {name}\nEmail: {email}\nNotes: {notes}',
        'no-reply@uoas.co.za',
        ['admin@uoas.co.za'],
        fail_silently=True,
    )
    messages.success(request, f"Requested quotation for {product.name}.")
    return redirect('products')

@require_POST
def add_to_cart(request, product_id):
    messages.error(request, "Cart functionality is not available.")
    return redirect('products')

def cart_view(request):
    return render(request, 'cart.html', {'cart_items': [], 'cart_total': 0})

@require_POST
def update_cart_item(request, item_id):
    messages.error(request, "Cart update functionality is not available.")
    return redirect('cart')

@require_POST
def remove_cart_item(request, item_id):
    messages.error(request, "Cart remove functionality is not available.")
    return redirect('cart')

def checkout_view(request):
    messages.error(request, "Checkout functionality is not available.")
    return render(request, 'checkout.html', {'cart_items': [], 'cart_total': 0})

def order_confirmation_view(request, order_id):
    messages.error(request, "Order confirmation is not available.")
    return render(request, 'order_confirmation.html', {})

def order_tracking(request):
    return render(request, 'order_tracking.html', {'orders': [], 'email': ''})

def order_detail(request, order_id, email):
    messages.error(request, "Order detail is not available.")
    return render(request, 'order_detail.html', {})

def cart_count(request):
    return 0
