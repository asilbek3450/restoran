import urllib.request
import urllib.parse
import json
from html import escape

from django.conf import settings


def send_telegram_message(text):
    """Telegram bot orqali admin ga xabar yuborish"""
    try:
        token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_ADMIN_CHAT_ID

        if token == 'YOUR_BOT_TOKEN_HERE' or chat_id == 'YOUR_CHAT_ID_HERE':
            print("⚠️  Telegram token yoki chat_id sozlanmagan!")
            return False

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = urllib.parse.urlencode({
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }).encode('utf-8')

        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read())
            return result.get('ok', False)
    except Exception as e:
        print(f"Telegram xato: {e}")
        return False


def notify_new_message(contact_message):
    """Yangi xabar kelganda adminni xabardor qilish"""
    text = (
        f"🔔 <b>Yangi xabar keldi!</b>\n\n"
        f"👤 <b>Ism:</b> {escape(contact_message.full_name)}\n"
        f"💬 <b>Xabar:</b>\n{escape(contact_message.message)}\n\n"
        f"🕐 <b>Vaqt:</b> {contact_message.created_at.strftime('%d.%m.%Y %H:%M')}"
    )
    return send_telegram_message(text)


def notify_new_reservation(reservation):
    """Yangi bron kelganda adminni xabardor qilish"""
    special_requests = reservation.special_requests or "Yoq"
    text = (
        f"📅 <b>Yangi bron yaratildi!</b>\n\n"
        f"👤 <b>Mijoz:</b> {escape(reservation.full_name)}\n"
        f"📞 <b>Telefon:</b> {escape(reservation.phone_number)}\n"
        f"👥 <b>Mehmonlar:</b> {reservation.guest_count} ta\n"
        f"🗓️ <b>Sana:</b> {reservation.reservation_date.strftime('%d.%m.%Y')}\n"
        f"⏰ <b>Vaqt:</b> {reservation.reservation_time.strftime('%H:%M')}\n"
        f"🪑 <b>Joy:</b> {escape(reservation.get_seating_preference_display())}\n"
        f"🎉 <b>Sabab:</b> {escape(reservation.get_occasion_display())}\n"
        f"📝 <b>Izoh:</b> {escape(special_requests)}\n\n"
        f"📌 <b>Status:</b> {escape(reservation.get_status_display())}\n"
        f"🕐 <b>Yuborilgan:</b> {reservation.created_at.strftime('%d.%m.%Y %H:%M')}"
    )
    return send_telegram_message(text)
