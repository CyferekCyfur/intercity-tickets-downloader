import imaplib
import os
import email


class EmailReader:
    def __init__(self, user, password, tickets_path, imap):
        self.user = user
        self.password = password
        self.tickets_path = tickets_path
        self.imap = imap
        self.data, self.mail_info = self.setup()
        self.download_attachments()

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_imap(self):
        return self.imap

    def get_tickets_path(self):
        return self.tickets_path

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

            for att in decoded_email.walk():
                if att.get_content_maintype() != 'multipart' and att.get(
                        'Content-Disposition') is not None:
                    filename = att.get_filename()
                    if not filename:
                        filename = "ticket.pdf"
                    attachment = att.get_payload(decode=True)
                    path = os.path.join(self.get_tickets_path(), filename)
                    with open(path, 'wb') as fp:
                        fp.write(attachment)
                        fp.close()

        self.mail_info.close()
        self.mail_info.logout()
