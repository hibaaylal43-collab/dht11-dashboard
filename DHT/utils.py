# DHT/utils.py
import requests
from django.conf import settings


def send_telegram(text: str):
    """
    Envoie un message Telegram en utilisant le bot défini
    dans settings.TELEGRAM_BOT_TOKEN et settings.TELEGRAM_CHAT_ID
    """
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": text,
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # lève une erreur si Telegram renvoie une erreur
    except Exception as e:
        print("Erreur envoi Telegram:", e)
