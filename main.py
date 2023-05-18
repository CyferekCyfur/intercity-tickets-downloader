from PDFCrop import PDFCrop
from EmailReader import EmailReader


def main():
    user = "your_mail"
    password = "your_password"
    imap = "imap_of_your_email"
    tickets_path = "/directory/where/you/want/to/save/pdfs/"
    qr_path = "/path/where/you/want/to/store/your/qrs/"

    e_read = EmailReader(user, password, tickets_path, imap)
    pdf = PDFCrop(tickets_path, qr_path)


if __name__ == "__main__":
    main()
