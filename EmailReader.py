import imaplib
import os
import email


class EmailReader:
    def __init__(self, user, password, dir, imap):
        self.user = user
        self.password = password
        self.dir = dir
        self.imap = imap
        self.data, self.mail_info = self.setup()

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_imap(self):
        return self.imap

    def setup(self):
        mail_info = imaplib.IMAP4_SSL(self.get_imap(), 993)
        mail_info.login(self.get_user(), self.get_password())
        mail_info.select("Inbox")
        _, data = mail_info.search(None, "FROM bilet.eic@intercity.pl")
        return data, mail_info

    def download_attachments(self):
        for id in self.data[0].split():
            _, content = self.mail_info.fetch(id, "(RFC822)")
            body = content[0][1].decode('utf-8')
            decoded_email = email.message_from_string(body)
            # mail_info.store(id, '+FLAGS', '\\Deleted')
            # mail_info.expunge()

            for att in decoded_email.walk():
                if att.get_content_maintype() != 'multipart' and att.get('Content-Disposition') is not None:
                    filename = att.get_filename()
                    print(filename)
                    if not filename:
                        filename = "ticket.pdf"
                    attachment = att.get_payload(decode=True)
                    path = os.path.join(dir, filename)
                    with open(path, 'wb') as fp:
                        fp.write(attachment)
                        fp.close()

        self.mail_info.close()
        self.mail_info.logout()


if __name__ == "__main__":
    user = "your_mail"
    password = "your_password"
    dir = "/directory/where/you/want/to/save/pdfs"
    imap = "imap_of_your_email"
    e_read = EmailReader(user, password, dir, imap)
    e_read.download_attachments()
