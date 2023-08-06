from PDFCrop import PDFCrop
from EmailReader import EmailReader
from TelegramBot import TelegramBot
import os
import asyncio


def main():
    user = "your_mail"
    password = "your_password"
    imap = "imap_of_your_email"
    tickets_path = "/directory/where/you/want/to/save/pdfs/"
    qr_path = "/path/where/you/want/to/store/your/qrs/"

    TOKEN = "telegram_bot_token"
    chat_id = 123456789 # your chat id

    e_read = EmailReader(user, password, tickets_path, imap)
    pdf = PDFCrop(tickets_path, qr_path)
    tg = TelegramBot(TOKEN, chat_id)

    loop = asyncio.get_event_loop()
    async def process_tickets():
        while True:
            e_read.download_attachments()
            pdf.scan_for_tickets(tickets_path)
            pdf.convert()
            pdf.crop_jpg()
            e_read.remove_attachments()
            if len(pdf.scan_for_tickets(qr_path)) != 0:
                for file in pdf.scan_for_tickets(qr_path):
                    await tg.send_message(qr_path + file)
                    os.remove(qr_path + file)

    loop.create_task(process_tickets())
    loop.run_forever()



if __name__ == "__main__":
    main()
