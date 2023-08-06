from telegram import Bot

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=self.token)
    async def send_message(self, qr):
        await self.bot.send_photo(chat_id=self.chat_id, photo=open(qr, 'rb'))
