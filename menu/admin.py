from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ContactMessage, Reservation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'order', 'product_count']
    list_editable = ['order']
    search_fields = ['name']

    def product_count(self, obj):
        count = obj.products.count()
        return format_html('<span style="font-weight:bold;color:#e67e22">{} ta</span>', count)
    product_count.short_description = "Mahsulotlar soni"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name', 'category', 'price_display', 'is_available', 'is_popular']
    list_editable = ['is_available', 'is_popular']
    list_filter = ['category', 'is_available', 'is_popular']
    search_fields = ['name', 'description']
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return format_html('<div style="width:60px;height:60px;background:#f0f0f0;border-radius:8px;display:flex;align-items:center;justify-content:center;">🍽️</div>')
    image_preview.short_description = "Rasm"

    def price_display(self, obj):
        return format_html('<strong style="color:#27ae60">{} so\'m</strong>', obj.formatted_price())
    price_display.short_description = "Narxi"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'short_message', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['full_name', 'message']
    readonly_fields = ['full_name', 'message', 'created_at']

    def short_message(self, obj):
        return obj.message[:80] + '...' if len(obj.message) > 80 else obj.message
    short_message.short_description = "Xabar"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        unread_count = ContactMessage.objects.filter(is_read=False).count()
        extra_context['unread_count'] = unread_count
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone_number',
        'guest_count',
        'reservation_date',
        'reservation_time',
        'status',
        'is_contacted',
    ]
    list_editable = ['status', 'is_contacted']
    list_filter = ['status', 'seating_preference', 'occasion', 'reservation_date']
    search_fields = ['full_name', 'phone_number', 'special_requests']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 25


# Admin panel dizaynini o'zgartirish
admin.site.site_header = "🍴 Dasturxon — Admin Panel"
admin.site.site_title = "Dasturxon"
admin.site.index_title = "Dasturxon boshqaruv paneliga xush kelibsiz"
