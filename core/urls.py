from django.urls import path
from .views import HomeView, OrderSummaryView, ItemDetailView, add_to_cart, remove_from_cart, checkout, remove_single_item_from_cart

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name= 'checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name= 'order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove_item_from_cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]