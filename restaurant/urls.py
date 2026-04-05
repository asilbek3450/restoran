from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu import views as menu_views
from menu import admin_views

urlpatterns = [
    # Asosiy sahifalar
    path('', menu_views.home, name='home'),
    path('menu/', menu_views.menu, name='menu'),
    path('about/', menu_views.about, name='about'),
    path('reservation/', menu_views.reservation, name='reservation'),
    path('contact/', menu_views.contact, name='contact'),
    path('product/<int:pk>/', menu_views.product_detail, name='product_detail'),
    # Savat
    path('cart/', menu_views.cart, name='cart'),
    path('cart/add/<int:pk>/', menu_views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', menu_views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', menu_views.clear_cart, name='clear_cart'),
    path('order/confirm/', menu_views.order_confirm, name='order_confirm'),
    # MAXFIY ADMIN PANEL
    path('kitchen-portal/', admin_views.admin_login, name='admin_login'),
    path('kitchen-portal/logout/', admin_views.admin_logout, name='admin_logout'),
    path('kitchen-portal/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('kitchen-portal/categories/', admin_views.admin_categories, name='admin_categories'),
    path('kitchen-portal/categories/add/', admin_views.admin_category_add, name='admin_category_add'),
    path('kitchen-portal/categories/edit/<int:pk>/', admin_views.admin_category_edit, name='admin_category_edit'),
    path('kitchen-portal/categories/delete/<int:pk>/', admin_views.admin_category_delete, name='admin_category_delete'),
    path('kitchen-portal/products/', admin_views.admin_products, name='admin_products'),
    path('kitchen-portal/products/add/', admin_views.admin_product_add, name='admin_product_add'),
    path('kitchen-portal/products/edit/<int:pk>/', admin_views.admin_product_edit, name='admin_product_edit'),
    path('kitchen-portal/products/delete/<int:pk>/', admin_views.admin_product_delete, name='admin_product_delete'),
    path('kitchen-portal/products/toggle/<int:pk>/', admin_views.admin_product_toggle, name='admin_product_toggle'),
    path('kitchen-portal/messages/', admin_views.admin_messages, name='admin_messages'),
    path('kitchen-portal/messages/<int:pk>/', admin_views.admin_message_detail, name='admin_message_detail'),
    path('kitchen-portal/messages/delete/<int:pk>/', admin_views.admin_message_delete, name='admin_message_delete'),
    path('kitchen-portal/reservations/', admin_views.admin_reservations, name='admin_reservations'),
    path('kitchen-portal/reservations/<int:pk>/', admin_views.admin_reservation_detail, name='admin_reservation_detail'),
    path('kitchen-portal/reservations/delete/<int:pk>/', admin_views.admin_reservation_delete, name='admin_reservation_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
