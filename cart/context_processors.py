from .models import Cart,CartItem
from .views import _cart_id


def count(request):
    items_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cart_items=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                items_count+=cart_item.quantity
        except Cart.DoesNotExist:
            items_count=0
    return dict(items_count=items_count)
