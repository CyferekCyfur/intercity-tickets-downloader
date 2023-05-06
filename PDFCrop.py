import os
from PyPDF2 import PdfReader, PdfWriter


class PDFCrop:
    def __init__(self, tickets_path, qr_path):
        self.tickets_path = tickets_path
        self.qr_path = qr_path
        self.files = None
        self.scan_for_tickets()
        self.crop_pdf()

    def get_qr_path(self):
        return self.qr_path
    def get_tickets_path(self):
        return self.tickets_path

    def get_files(self):
        return self.files

    def set_files(self, x):
        self.files = x

    def scan_for_tickets(self):

        file_type = "pdf"

        files = os.listdir(tickets_path)
        files = [file for file in files if file.split('.')[-1] == file_type]
        self.set_files(files)

    def crop_pdf(self):
        for file in self.get_files():
            read_qr = PdfReader(os.path.join(self.get_tickets_path(), file))
            write_qr = PdfWriter()
            read_qr.pages[0].cropbox.upper_left = (0, 500)
            read_qr.pages[0].cropbox.lower_right = (1000, 1000)
            write_qr.add_page(read_qr.pages[0])

            if not os.path.isdir(self.get_qr_path()):
                os.mkdir(self.get_qr_path())
            with open(self.get_qr_path() + "/qr_" + file, 'wb') as fp:
                write_qr.write(fp)

            del read_qr
            del write_qr


if __name__ == "__main__":
    tickets_path = "/path/where/you/store/your/tickets"
    qr_path = "/path/where/you/want/to/store/your/qrs"
    pdf = PDFCrop(tickets_path, qr_path)
