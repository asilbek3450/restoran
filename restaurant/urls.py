from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from menu import views as menu_views
from menu import admin_views
from django.contrib.sitemaps.views import sitemap
from menu.sitemaps import StaticViewSitemap, ProductSitemap, CategorySitemap
from django.http import HttpResponse

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    # Asosiy sahifalar
    path('', menu_views.home, name='home'),
    path('menu/', menu_views.menu, name='menu'),
    path('menu/<slug:slug>/', menu_views.menu, name='menu_category'),
    path('about/', menu_views.about, name='about'),
    path('reservation/', menu_views.reservation, name='reservation'),
    path('contact/', menu_views.contact, name='contact'),
    path('product/<slug:slug>/', menu_views.product_detail, name='product_detail'),
    
    # Savat
    path('cart/', menu_views.cart, name='cart'),
    path('cart/add/<int:pk>/', menu_views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', menu_views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', menu_views.clear_cart, name='clear_cart'),
    path('order/confirm/', menu_views.order_confirm, name='order_confirm'),
    
    # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nAllow: /\nSitemap: https://restoran.mirolimov.uz/sitemap.xml", content_type="text/plain")),
    
    path('googleef6572d0f05659ed.html', lambda r: HttpResponse("google-site-verification: googleef6572d0f05659ed.html", content_type="text/html")),
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
]

# O'zgarish: Railway (production) muhitida ham media fayllarni ko'rsatish uchun 
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
