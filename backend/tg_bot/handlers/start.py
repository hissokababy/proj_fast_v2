
def register_start_handlers(bot):

    @bot.message_handler(commands=["start"])
    def start_command(message):
        bot.send_message(
            message.chat.id,
            "FAST and EASY — бот языкового центра.\n\n"
            "Бот используется для уведомлений и управления "
            "служебными функциями."
        )

    @bot.message_handler(commands=["help"])
    def help_command(message):
        bot.send_message(
            message.chat.id,
            "Доступные команды:\n"
            "/start — информация о боте\n"
            "/help — список команд"
        )
