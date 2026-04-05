from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import ContactMessageForm, ReservationForm
from .models import Category, Product
from .telegram_bot import notify_new_message, notify_new_reservation


def home(request):
    categories = Category.objects.all()
    popular_products = Product.objects.filter(is_popular=True, is_available=True)[:6]
    return render(request, 'home.html', {
        'categories': categories,
        'popular_products': popular_products,
    })


def menu(request):
    categories = Category.objects.prefetch_related('products')
    selected_category = request.GET.get('category', 'all')

    if selected_category != 'all':
        products = Product.objects.filter(
            category__id=selected_category, is_available=True
        ).select_related('category')
    else:
        products = Product.objects.filter(is_available=True).select_related('category')

    return render(request, 'menu.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_available=True)
    related = Product.objects.filter(
        category=product.category, is_available=True
    ).exclude(pk=pk)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'related': related,
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            notify_new_message(contact_msg)
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi. Tez orada bog'lanamiz.")
            return redirect('contact')
        messages.error(request, "Iltimos, forma maydonlarini to'g'ri to'ldiring.")
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_obj = form.save()
            notify_new_reservation(reservation_obj)
            messages.success(
                request,
                "Broningiz qabul qilindi. Tez orada siz bilan bog'lanamiz.",
            )
            return redirect('reservation')
        messages.error(request, "Iltimos, bron formasi maydonlarini qayta tekshirib chiqing.")
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})


def cart(request):
    cart_data = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():
        try:
            product = Product.objects.get(pk=int(product_id))
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            pass

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'total_formatted': f"{int(total):,}".replace(",", " "),
    })


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk, is_available=True)
    cart = request.session.get('cart', {})
    key = str(pk)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    request.session.modified = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        total_items = sum(cart.values())
        return JsonResponse({'success': True, 'total_items': total_items, 'message': f"{product.name} savatga qo'shildi!"})
    return redirect(request.META.get('HTTP_REFERER', 'menu'))


def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    key = str(pk)
    if key in cart:
        if cart[key] > 1:
            cart[key] -= 1
        else:
            del cart[key]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')


def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('cart')


def order_confirm(request):
    """Buyurtmani tasdiqlash (savat tozalash bilan)"""
    if request.method == 'POST':
        cart_data = request.session.get('cart', {})
        if cart_data:
            # Bu yerda order saqlash logikasi qo'shishingiz mumkin
            request.session['cart'] = {}
            request.session.modified = True
            messages.success(request, "🎉 Buyurtmangiz qabul qilindi!")
    return redirect('home')
