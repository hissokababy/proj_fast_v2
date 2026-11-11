
import logging
import os

import requests
from django.utils import timezone

logger = logging.getLogger(__name__)


def send_application_notification(application):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        logger.warning(
            "Telegram notification skipped: credentials are not configured."
        )
        return False

    message = (
        "Новая заявка с сайта FAST and EASY\n\n"
        f"Имя: {application.full_name}\n"
        f"Телефон: {application.phone}\n"
        f"Язык сайта: {application.language or 'не указан'}\n"
        f"Дата: {application.created_at:%d.%m.%Y %H:%M}\n"
        f"UTM Source: {application.utm_source or '-'}\n"
        f"UTM Medium: {application.utm_medium or '-'}\n"
        f"UTM Campaign: {application.utm_campaign or '-'}\n"
        f"Страница: {application.landing_page or '-'}"
    )

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        response = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": message,
            },
            timeout=5,
        )
        response.raise_for_status()

        result = response.json()
        if not result.get("ok"):
            return False

        application.telegram_notified_at = timezone.now()
        application.save(update_fields=["telegram_notified_at"])

        return True

    except (requests.RequestException, ValueError):
        logger.exception(
            "Failed to send Telegram notification for application %s",
            application.pk,
        )
        return False
