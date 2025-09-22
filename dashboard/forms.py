from django import forms
from printerapp.models import Product, Slide, QuotationRequest, TeamMember

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_url', 'image', 'product_type', 'in_stock']

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['image_url', 'image', 'location', 'project_link']

class QuotationRequestForm(forms.ModelForm):
    class Meta:
        model = QuotationRequest
        fields = ['product', 'quantity', 'email', 'notes']

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'email', 'image', 'department']
