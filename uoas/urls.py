"""
URL configuration for uoas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, about, contact, it_page, printer, solar, printer_detail, solar_projects, order_tracking, products, product_detail
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from printerapp.views import add_to_cart, add_to_quote, cart_view, update_cart_item, remove_cart_item, checkout_view, order_detail, order_confirmation_view

urlpatterns = [
    path('', home, name='home'),
    path('index.html', home, name='home_index'),
    path('about.html', about, name='about'),
    path('contact.html', contact, name='contact'),
    path('it.html', it_page, name='it'),
    path('printer.html', printer, name='printer'),
    path('printer/<int:pk>/', printer_detail, name='printer_detail'),
    path('solar.html', solar, name='solar'),
    path('solar/', solar, name='solar'),
    path('solar-projects.html', solar_projects, name='solar_projects'),
    path('office-printer.html', RedirectView.as_view(url='/printer.html', permanent=True)),
    path('products/', products, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('quote/add/<int:product_id>/', add_to_quote, name='add_to_quote'),
    path('cart/', cart_view, name='cart'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
    path('checkout/', checkout_view, name='checkout'),
    path('order-confirmation/<int:order_id>/', order_confirmation_view, name='order_confirmation'),
    path('order-tracking/', order_tracking, name='order_tracking'),
    path('order/<int:order_id>/<str:email>/', order_detail, name='order_detail'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
