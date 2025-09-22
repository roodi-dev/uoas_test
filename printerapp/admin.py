from django.contrib import admin
from django.core.mail import send_mail
from .models import Printer, Slide, Product, QuotationRequest, TeamMember

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('location', 'image_url', 'project_link')
    search_fields = ('location',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'in_stock')
    search_fields = ('name', 'product_type')
    list_filter = ('product_type', 'in_stock')


@admin.register(QuotationRequest)
class QuotationRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'email', 'requested_at', 'notes')
    search_fields = ('product__name', 'email', 'notes')
    list_filter = ('requested_at', 'product')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'position', 'email')



