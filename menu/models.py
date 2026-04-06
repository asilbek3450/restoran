from django.db import models


from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    icon = models.CharField(max_length=50, default="🍽️", verbose_name="Emoji icon")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Kategoriya")
    name = models.CharField(max_length=200, verbose_name="Mahsulot nomi")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Narxi (so'm)")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Rasm")
    is_available = models.BooleanField(default=True, verbose_name="Mavjud")
    is_popular = models.BooleanField(default=False, verbose_name="Mashhur")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-is_popular', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def formatted_price(self):
        return f"{int(self.price):,}".replace(",", " ")


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Ism familiya")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name="O'qildi")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%d.%m.%Y %H:%M')}"


class Reservation(models.Model):
    class SeatingPreference(models.TextChoices):
        MAIN_HALL = 'main_hall', "Asosiy zal"
        TERRACE = 'terrace', "Terrasa"
        FAMILY_AREA = 'family_area', "Oilaviy zona"
        VIP_ROOM = 'vip_room', "VIP xona"

    class Occasion(models.TextChoices):
        CASUAL = 'casual', "Oddiy tashrif"
        FAMILY_DINNER = 'family_dinner', "Oilaviy kechki ovqat"
        BUSINESS = 'business', "Biznes uchrashuv"
        BIRTHDAY = 'birthday', "Tug'ilgan kun"
        ROMANTIC = 'romantic', "Romantik kecha"

    class Status(models.TextChoices):
        PENDING = 'pending', "Kutilmoqda"
        CONFIRMED = 'confirmed', "Tasdiqlangan"
        COMPLETED = 'completed', "Yakunlangan"
        CANCELLED = 'cancelled', "Bekor qilingan"

    full_name = models.CharField(max_length=120, verbose_name="Mijoz ismi")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami")
    guest_count = models.PositiveSmallIntegerField(verbose_name="Mehmonlar soni")
    reservation_date = models.DateField(db_index=True, verbose_name="Bron sanasi")
    reservation_time = models.TimeField(verbose_name="Bron vaqti")
    seating_preference = models.CharField(
        max_length=20,
        choices=SeatingPreference.choices,
        default=SeatingPreference.MAIN_HALL,
        verbose_name="Joylashuv",
    )
    occasion = models.CharField(
        max_length=20,
        choices=Occasion.choices,
        default=Occasion.CASUAL,
        verbose_name="Tashrif sababi",
    )
    special_requests = models.TextField(blank=True, verbose_name="Qo'shimcha izoh")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
        verbose_name="Holati",
    )
    is_contacted = models.BooleanField(default=False, verbose_name="Bog'lanildi")
    admin_note = models.TextField(blank=True, verbose_name="Admin eslatmasi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bron"
        verbose_name_plural = "Bronlar"
        ordering = ['reservation_date', 'reservation_time', '-created_at']

    def __str__(self):
        return (
            f"{self.full_name} - "
            f"{self.reservation_date.strftime('%d.%m.%Y')} {self.reservation_time.strftime('%H:%M')}"
        )

    def formatted_schedule(self):
        return f"{self.reservation_date.strftime('%d.%m.%Y')} / {self.reservation_time.strftime('%H:%M')}"
