from django.contrib import admin
from .models import *

admin.site.register(
    (
        Maincategory,
        Subcategory,
        Brand,
        Seller,
        Buyer,
        Product,
        Wishlist,
        Newslatter,
        Checkout,
        CheckoutProducts,
        Contact,
        
    )
)
