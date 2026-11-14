
import logging

from django.core.management.base import BaseCommand, CommandError

from tg_bot.bot import create_bot


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Запуск Telegram-бота FAST and EASY"

    def handle(self, *args, **options):
        try:
            bot = create_bot()
        except ValueError as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(
            self.style.SUCCESS("Telegram-бот запущен.")
        )

        try:
            bot.infinity_polling(
                skip_pending=True,
                timeout=20,
                long_polling_timeout=20,
            )
        except KeyboardInterrupt:
            self.stdout.write("Telegram-бот остановлен.")
        except Exception:
            logger.exception("Telegram bot stopped unexpectedly.")
            raise
