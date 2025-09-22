from django.db import models
from django.contrib.auth.models import User

class Printer(models.Model):
    CATEGORY_CHOICES = [
        ('small', 'Small Business Solutions'),
        ('large', 'Large Business Solutions'),
        ('other', 'Other Printing Solutions'),
    ]

    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    description = models.TextField()
    features = models.JSONField(blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='small')

    def __str__(self):
        return self.name

class Slide(models.Model):
    image_url = models.URLField(max_length=500, blank=True)
    image = models.ImageField(upload_to='slides/', blank=True, null=True)
    location = models.CharField(max_length=200)
    project_link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.location

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('printer', 'Printer'),
        ('ip_phone', 'IP Phone'),
        ('it_solution', 'IT Solution'),
        ('networking', 'Networking'),
        ('parrot', 'Parrot'),
        ('solar', 'Solar'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class QuotationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    requested_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Quote for {self.product.name} x {self.quantity}"

class TeamMember(models.Model):
    DEPARTMENT_CHOICES = [
        ('office_printer', 'Office Printer Department'),
        ('solar', 'Solar Department'),
        ('it', 'IT Department'),
    ]

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.get_department_display()}"


