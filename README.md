# intercity-tickets-downloader
## General info
This script is a PKP Intercity tickets downloader.

## Dependencies
To run this project, you will have to install undermentioned libraries:
* PyPDF2
* email
* imaplib
* pillow
* pdf2image

## Setup
1. Create your telegram bot using @BotFather
2. Get your chat_id using @RawDataBot
3. In the main part of script change your email, password, directory, where you want to temporary store your tickets, directory, where you want to temporary store your qr codes (they mustn't be the same directory) and imap of your mail. 
4. Change TOKEN to your bot token and change chat_id to your chat_id
5. Run the main.py:
```
$ python3 main.py
```
