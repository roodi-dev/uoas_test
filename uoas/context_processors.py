from django.db.models import Sum

def cart_item_count(request):
    # Simple cart count implementation without CartItem model
    # For now, return 0 as we're removing CartItem completely
    return {'cart_item_count': 0}
