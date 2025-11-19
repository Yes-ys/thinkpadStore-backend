from django.contrib import admin
from .models import User, Product, Cart
from .models import CartItem

#admin.site.register(User)
#admin.site.register(Product)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'username']  # Enable search by email and username

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'model']  # Enable search by name and model


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    search_fields = ['user__username', 'user__email']  # Enable search by user's username and email


admin.site.register(Cart, CartAdmin)
