from datetime import timedelta
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import ContactMessage, Reservation


class ContactAndReservationTests(TestCase):
    @patch('menu.views.notify_new_message')
    def test_contact_form_creates_message_and_sends_notification(self, mock_notify):
        response = self.client.post(reverse('contact'), {
            'full_name': 'Ali Valiyev',
            'message': 'Salom, menyu bo\'yicha savolim bor.',
        })

        self.assertRedirects(response, reverse('contact'))
        self.assertEqual(ContactMessage.objects.count(), 1)
        mock_notify.assert_called_once()

    @patch('menu.views.notify_new_reservation')
    def test_reservation_form_creates_record_and_sends_notification(self, mock_notify):
        target_datetime = timezone.localtime() + timedelta(days=1)
        response = self.client.post(reverse('reservation'), {
            'full_name': 'Dilshod Rahimov',
            'phone_number': '+998901234567',
            'guest_count': 4,
            'reservation_date': target_datetime.date().isoformat(),
            'reservation_time': '19:30',
            'seating_preference': Reservation.SeatingPreference.TERRACE,
            'occasion': Reservation.Occasion.BIRTHDAY,
            'special_requests': 'Deraza yonida stol bo\'lsa yaxshi bo\'lardi.',
        })

        self.assertRedirects(response, reverse('reservation'))
        self.assertEqual(Reservation.objects.count(), 1)
        reservation = Reservation.objects.get()
        self.assertEqual(reservation.phone_number, '+998901234567')
        self.assertEqual(reservation.status, Reservation.Status.PENDING)
        mock_notify.assert_called_once_with(reservation)

    def test_reservation_form_rejects_too_soon_booking(self):
        soon_datetime = timezone.localtime() + timedelta(minutes=20)
        response = self.client.post(reverse('reservation'), {
            'full_name': 'Short Notice',
            'phone_number': '+998901234567',
            'guest_count': 2,
            'reservation_date': soon_datetime.date().isoformat(),
            'reservation_time': soon_datetime.strftime('%H:%M'),
            'seating_preference': Reservation.SeatingPreference.MAIN_HALL,
            'occasion': Reservation.Occasion.CASUAL,
            'special_requests': '',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "45 daqiqadan keyin")
        self.assertEqual(Reservation.objects.count(), 0)
