from datetime import datetime, time, timedelta

from django import forms
from django.utils import timezone

from .models import ContactMessage, Reservation


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': "Masalan: Alisher Karimov",
                'autocomplete': 'name',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': "Savol yoki taklifingizni yozing...",
                'rows': 5,
            }),
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'full_name',
            'phone_number',
            'guest_count',
            'reservation_date',
            'reservation_time',
            'seating_preference',
            'occasion',
            'special_requests',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'booking-input',
                'placeholder': "Masalan: Dilshod Rahimov",
                'autocomplete': 'name',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'booking-input',
                'placeholder': "+998 90 123 45 67",
                'autocomplete': 'tel',
                'inputmode': 'tel',
            }),
            'guest_count': forms.NumberInput(attrs={
                'class': 'booking-input',
                'min': 1,
                'max': 16,
            }),
            'reservation_date': forms.DateInput(attrs={
                'class': 'booking-input',
                'type': 'date',
            }),
            'reservation_time': forms.TimeInput(attrs={
                'class': 'booking-input',
                'type': 'time',
                'step': 1800,
            }),
            'seating_preference': forms.Select(attrs={'class': 'booking-select'}),
            'occasion': forms.Select(attrs={'class': 'booking-select'}),
            'special_requests': forms.Textarea(attrs={
                'class': 'booking-textarea',
                'rows': 4,
                'placeholder': "Bolalar stuli, deraza yonida stol, tug'ilgan kun bezagi va hokazo.",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = timezone.localdate()
        self.fields['reservation_date'].widget.attrs['min'] = today.isoformat()
        self.fields['reservation_date'].initial = today + timedelta(days=1)
        self.fields['reservation_time'].initial = time(hour=19, minute=0)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number'].strip()
        digits_only = ''.join(ch for ch in phone_number if ch.isdigit())

        if len(digits_only) == 9:
            return f"+998{digits_only}"

        if len(digits_only) == 12 and digits_only.startswith('998'):
            return f"+{digits_only}"

        if 9 <= len(digits_only) <= 15:
            return f"+{digits_only}"

        raise forms.ValidationError("Telefon raqamini to'g'ri formatda kiriting.")

    def clean_guest_count(self):
        guest_count = self.cleaned_data['guest_count']
        if guest_count < 1:
            raise forms.ValidationError("Kamida 1 mehmon bo'lishi kerak.")
        if guest_count > 16:
            raise forms.ValidationError("Bir bron orqali maksimum 16 mehmon qabul qilinadi.")
        return guest_count

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_time = cleaned_data.get('reservation_time')

        if not reservation_date or not reservation_time:
            return cleaned_data

        if reservation_time < time(hour=9, minute=0) or reservation_time > time(hour=22, minute=0):
            self.add_error(
                'reservation_time',
                "Bron vaqti 09:00 dan 22:00 gacha bo'lishi kerak.",
            )

        if reservation_date > timezone.localdate() + timedelta(days=90):
            self.add_error(
                'reservation_date',
                "Bronni faqat keyingi 90 kun oralig'ida yaratish mumkin.",
            )

        current_time = timezone.localtime()
        reservation_dt = timezone.make_aware(
            datetime.combine(reservation_date, reservation_time),
            timezone.get_current_timezone(),
        )

        if reservation_dt < current_time + timedelta(minutes=45):
            self.add_error(
                'reservation_time',
                "Eng yaqin bron kamida 45 daqiqadan keyin bo'lishi kerak.",
            )

        return cleaned_data
