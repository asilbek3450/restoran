import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone

from .models import Category, Product, ContactMessage, Reservation


def _admin_ctx(request):
    """Sidebar uchun umumiy context"""
    return {
        'sidebar_unread': ContactMessage.objects.filter(is_read=False).count(),
        'sidebar_pending_reservations': Reservation.objects.filter(
            status=Reservation.Status.PENDING
        ).count(),
    }


# ─── LOGIN REQUIRED DECORATOR ──────────────────────────────────────────────────
def admin_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_kitchen_admin'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


# ─── LOGIN ─────────────────────────────────────────────────────────────────────
def admin_login(request):
    if request.session.get('is_kitchen_admin'):
        return redirect('admin_dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        from django.conf import settings
        admin_user = getattr(settings, 'KITCHEN_ADMIN_USER', 'admin')
        admin_pass = getattr(settings, 'KITCHEN_ADMIN_PASS', 'dasturxon2025')
        if username == admin_user and password == admin_pass:
            request.session['is_kitchen_admin'] = True
            request.session['admin_username'] = username
            return redirect('admin_dashboard')
        else:
            error = "Foydalanuvchi nomi yoki parol noto'g'ri!"
    return render(request, 'admin_panel/login.html', {'error': error})


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# ─── DASHBOARD ─────────────────────────────────────────────────────────────────
@admin_login_required
def admin_dashboard(request):
    today = timezone.localdate()
    ctx = _admin_ctx(request)
    ctx.update({
        'total_categories': Category.objects.count(),
        'total_products': Product.objects.count(),
        'available_products': Product.objects.filter(is_available=True).count(),
        'popular_products': Product.objects.filter(is_popular=True).count(),
        'total_messages': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'total_reservations': Reservation.objects.count(),
        'pending_reservations': Reservation.objects.filter(status=Reservation.Status.PENDING).count(),
        'today_reservations': Reservation.objects.filter(reservation_date=today).count(),
        'recent_messages': ContactMessage.objects.order_by('-created_at')[:5],
        'recent_reservations': Reservation.objects.order_by('-created_at')[:5],
        'categories_with_count': Category.objects.annotate(cnt=Count('products')).order_by('-cnt')[:5],
        'recent_products': Product.objects.select_related('category').order_by('-created_at')[:6],
    })
    return render(request, 'admin_panel/dashboard.html', ctx)


# ─── CATEGORIES ────────────────────────────────────────────────────────────────
@admin_login_required
def admin_categories(request):
    ctx = _admin_ctx(request)
    ctx['categories'] = Category.objects.annotate(cnt=Count('products')).order_by('order', 'name')
    return render(request, 'admin_panel/categories.html', ctx)


@admin_login_required
def admin_category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        icon = request.POST.get('icon', '🍽️').strip()
        order = request.POST.get('order', 0)
        if name:
            Category.objects.create(name=name, icon=icon, order=int(order))
            messages.success(request, f"✅ '{name}' kategoriyasi qo'shildi!")
            return redirect('admin_categories')
        else:
            messages.error(request, "❌ Kategoriya nomi kiritilmadi!")
    ctx = _admin_ctx(request)
    ctx['action'] = 'add'
    return render(request, 'admin_panel/category_form.html', ctx)


@admin_login_required
def admin_category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        icon = request.POST.get('icon', '🍽️').strip()
        order = request.POST.get('order', 0)
        if name:
            category.name = name
            category.icon = icon
            category.order = int(order)
            category.save()
            messages.success(request, f"✅ '{name}' yangilandi!")
            return redirect('admin_categories')
    ctx = _admin_ctx(request)
    ctx.update({'action': 'edit', 'category': category})
    return render(request, 'admin_panel/category_form.html', ctx)


@admin_login_required
def admin_category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f"🗑️ '{name}' o'chirildi!")
    return redirect('admin_categories')


# ─── PRODUCTS ──────────────────────────────────────────────────────────────────
@admin_login_required
def admin_products(request):
    qs = Product.objects.select_related('category').order_by('-created_at')
    cat_filter = request.GET.get('category', '')
    search = request.GET.get('search', '')
    if cat_filter:
        qs = qs.filter(category__id=cat_filter)
    if search:
        qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
    ctx = _admin_ctx(request)
    ctx.update({
        'products': qs,
        'categories': Category.objects.all(),
        'cat_filter': cat_filter,
        'search': search,
    })
    return render(request, 'admin_panel/products.html', ctx)


@admin_login_required
def admin_product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        category_id = request.POST.get('category')
        description = request.POST.get('description', '').strip()
        price_raw = request.POST.get('price', '0').replace(' ', '').replace(',', '')
        is_available = request.POST.get('is_available') == 'on'
        is_popular = request.POST.get('is_popular') == 'on'
        image = request.FILES.get('image')
        if name and category_id:
            price = int(price_raw) if price_raw.isdigit() else 0
            product = Product.objects.create(
                name=name, category_id=int(category_id),
                description=description, price=price,
                is_available=is_available, is_popular=is_popular,
            )
            if image:
                product.image = image
                product.save()
            messages.success(request, f"✅ '{name}' mahsuloti qo'shildi!")
            return redirect('admin_products')
        else:
            messages.error(request, "❌ Nom va kategoriya majburiy!")
    ctx = _admin_ctx(request)
    ctx.update({'action': 'add', 'categories': Category.objects.all()})
    return render(request, 'admin_panel/product_form.html', ctx)


@admin_login_required
def admin_product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name', '').strip()
        product.category_id = int(request.POST.get('category', product.category_id))
        product.description = request.POST.get('description', '').strip()
        price_raw = request.POST.get('price', '0').replace(' ', '').replace(',', '')
        product.price = int(price_raw) if price_raw.isdigit() else product.price
        product.is_available = request.POST.get('is_available') == 'on'
        product.is_popular = request.POST.get('is_popular') == 'on'
        image = request.FILES.get('image')
        if image:
            if product.image:
                try:
                    os.remove(product.image.path)
                except Exception:
                    pass
            product.image = image
        product.save()
        messages.success(request, f"✅ '{product.name}' yangilandi!")
        return redirect('admin_products')
    ctx = _admin_ctx(request)
    ctx.update({'action': 'edit', 'product': product, 'categories': Category.objects.all()})
    return render(request, 'admin_panel/product_form.html', ctx)


@admin_login_required
def admin_product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name = product.name
        if product.image:
            try:
                os.remove(product.image.path)
            except Exception:
                pass
        product.delete()
        messages.success(request, f"🗑️ '{name}' o'chirildi!")
    return redirect('admin_products')


@admin_login_required
def admin_product_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_available = not product.is_available
    product.save()
    return JsonResponse({
        'success': True,
        'is_available': product.is_available,
        'status': "mavjud" if product.is_available else "mavjud emas"
    })


# ─── MESSAGES ──────────────────────────────────────────────────────────────────
@admin_login_required
def admin_messages(request):
    ctx = _admin_ctx(request)
    msgs = ContactMessage.objects.order_by('-created_at')
    ctx.update({'msgs': msgs, 'unread': msgs.filter(is_read=False).count()})
    return render(request, 'admin_panel/messages.html', ctx)


@admin_login_required
def admin_message_detail(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if not msg.is_read:
        msg.is_read = True
        msg.save()
    ctx = _admin_ctx(request)
    ctx['msg'] = msg
    return render(request, 'admin_panel/message_detail.html', ctx)


@admin_login_required
def admin_message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        msg.delete()
        messages.success(request, "🗑️ Xabar o'chirildi!")
    return redirect('admin_messages')


# ─── RESERVATIONS ──────────────────────────────────────────────────────────────
@admin_login_required
def admin_reservations(request):
    reservations = Reservation.objects.order_by('reservation_date', 'reservation_time', '-created_at')
    status_filter = request.GET.get('status', '').strip()
    search = request.GET.get('search', '').strip()

    if status_filter:
        reservations = reservations.filter(status=status_filter)

    if search:
        reservations = reservations.filter(
            Q(full_name__icontains=search)
            | Q(phone_number__icontains=search)
            | Q(special_requests__icontains=search)
        )

    ctx = _admin_ctx(request)
    ctx.update({
        'reservations': reservations,
        'status_filter': status_filter,
        'search': search,
        'statuses': Reservation.Status.choices,
        'reservation_count': reservations.count(),
    })
    return render(request, 'admin_panel/reservations.html', ctx)


@admin_login_required
def admin_reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        status = request.POST.get('status', reservation.status)
        valid_statuses = {choice[0] for choice in Reservation.Status.choices}
        reservation.status = status if status in valid_statuses else reservation.status
        reservation.is_contacted = request.POST.get('is_contacted') == 'on'
        reservation.admin_note = request.POST.get('admin_note', '').strip()
        reservation.save()
        messages.success(request, "Bron ma'lumotlari yangilandi.")
        return redirect('admin_reservation_detail', pk=reservation.pk)

    ctx = _admin_ctx(request)
    ctx.update({
        'reservation': reservation,
        'statuses': Reservation.Status.choices,
    })
    return render(request, 'admin_panel/reservation_detail.html', ctx)


@admin_login_required
def admin_reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Bron o'chirildi.")
    return redirect('admin_reservations')
