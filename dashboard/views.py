from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Manager
from django.http import HttpResponse
from printerapp.models import Product, Slide, QuotationRequest, TeamMember
from .forms import ProductForm, SlideForm, QuotationRequestForm, TeamMemberForm
from functools import wraps


# Decorator for manager authentication
def manager_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('manager_id'):
            return redirect('dashboard_login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@manager_required
def slide_list(request):
    slides = Slide.objects.all()
    return render(request, 'dashboard/slide_list.html', {'slides': slides})

@manager_required
def slide_add(request):
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slide added successfully!')
            return redirect('dashboard_slide_list')
    else:
        form = SlideForm()
    return render(request, 'dashboard/slide_form.html', {'form': form, 'action': 'Add'})

@manager_required
def slide_edit(request, pk):
    slide = get_object_or_404(Slide, pk=pk)
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slide updated successfully!')
            return redirect('dashboard_slide_list')
    else:
        form = SlideForm(instance=slide)
    return render(request, 'dashboard/slide_form.html', {'form': form, 'action': 'Edit'})

@manager_required
def slide_delete(request, pk):
    slide = get_object_or_404(Slide, pk=pk)
    if request.method == 'POST':
        slide.delete()
        messages.success(request, 'Slide deleted successfully!')
        return redirect('dashboard_slide_list')
    return render(request, 'dashboard/slide_confirm_delete.html', {'slide': slide})

@manager_required
def quotationrequest_list(request):
    requests = QuotationRequest.objects.select_related('product').all().order_by('-requested_at')
    return render(request, 'dashboard/quotationrequest_list.html', {'requests': requests})

@manager_required
def quotationrequest_detail(request, pk):
    quotation = get_object_or_404(QuotationRequest, pk=pk)
    return render(request, 'dashboard/quotationrequest_detail.html', {'quotation': quotation})

@manager_required
def quotationrequest_delete(request, pk):
    quotation = get_object_or_404(QuotationRequest, pk=pk)
    if request.method == 'POST':
        quotation.delete()
        messages.success(request, 'Quotation request deleted successfully!')
        return redirect('dashboard_quotationrequest_list')
    return render(request, 'dashboard/quotationrequest_confirm_delete.html', {'quotation': quotation})

def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            manager = Manager.objects.get(username=username, is_active=True)
            if check_password(password, manager.password):
                request.session['manager_id'] = manager.id
                return redirect('dashboard_home')
            else:
                messages.error(request, 'Invalid credentials.')
        except Manager.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'dashboard/login.html')

def manager_logout(request):
    request.session.flush()
    return redirect('dashboard_login')

def dashboard_home(request):
    manager_id = request.session.get('manager_id')
    if not manager_id:
        return redirect('dashboard_login')
    manager = Manager.objects.get(id=manager_id)

    # Get counts for dashboard stats
    products_count = Product.objects.count()
    slides_count = Slide.objects.count()
    quotations_count = QuotationRequest.objects.count()
    team_count = TeamMember.objects.count()

    context = {
        'manager': manager,
        'products_count': products_count,
        'slides_count': slides_count,
        'quotations_count': quotations_count,
        'team_count': team_count,
    }
    return render(request, 'dashboard/home.html', context)

@manager_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product_list.html', {'products': products})

@manager_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('dashboard_product_list')
    else:
        form = ProductForm()
    return render(request, 'dashboard/product_form.html', {'form': form, 'action': 'Add'})

@manager_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('dashboard_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/product_form.html', {'form': form, 'action': 'Edit'})

@manager_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('dashboard_product_list')
    return render(request, 'dashboard/product_confirm_delete.html', {'product': product})

@manager_required
def team_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'dashboard/team_list.html', {'team_members': team_members})

@manager_required
def team_add(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member added successfully!')
            return redirect('dashboard_team_list')
    else:
        form = TeamMemberForm()
    return render(request, 'dashboard/team_form.html', {'form': form, 'action': 'Add'})

@manager_required
def team_edit(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=team_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member updated successfully!')
            return redirect('dashboard_team_list')
    else:
        form = TeamMemberForm(instance=team_member)
    return render(request, 'dashboard/team_form.html', {'form': form, 'action': 'Edit'})

@manager_required
def team_delete(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        team_member.delete()
        messages.success(request, 'Team member deleted successfully!')
        return redirect('dashboard_team_list')
    return render(request, 'dashboard/team_confirm_delete.html', {'team_member': team_member})
