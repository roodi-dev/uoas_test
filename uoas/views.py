from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from printerapp.models import Printer, Slide, TeamMember

def printer(request):
    """
    View function for the office printer page.
    """
    printers_small = Printer.objects.filter(category='small')
    printers_large = Printer.objects.filter(category='large')
    printers_other = Printer.objects.filter(category='other')
    return render(request, 'printer.html', {
        'printers_small': printers_small,
        'printers_large': printers_large,
        'printers_other': printers_other,
    })

def printer_detail(request, pk):
    """
    View function for the printer detail page.
    """
    printer = get_object_or_404(Printer, pk=pk)
    return render(request, 'printer_detail.html', {'printer': printer})

def home(request):
    return render(request, 'index.html')

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', {'team_members': team_members})

def it_page(request):
    return render(request, 'it.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            messages.error(request, 'Please fill in all fields.')
            return redirect('contact')

        # Send email (configure email backend in settings.py)
        try:
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your message. We will get back to you soon.')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')

        return redirect('contact')

    return render(request, 'contact.html')

def solar(request):
    """
    View function for the solar page.
    """
    slides = Slide.objects.all()
    return render(request, 'solar.html', {'slides': slides})

def solar_projects(request):
    """
    View function for the solar projects page.
    """
    projects = Slide.objects.all()
    return render(request, 'solar_projects.html', {'projects': projects})

def order_tracking(request):
    """
    View function for the order tracking page.
    """
    return render(request, 'order_tracking.html')

from printerapp.models import Product
from django.shortcuts import get_object_or_404

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
