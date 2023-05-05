import os
# from pyPdf import PdfFileWriter, PdfFileReader


class PDFCrop:
    def __init__(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def scan_for_tickets(self):

        file_type = "pdf"

        files = os.listdir(path)
        files = [file for file in files if file.split('.')[-1] == file_type]
        return

    def crop_pdf(self):
        pass


if __name__ == "__main__":
    path = "/home/think/Documents/projekt bot telegram/tickets"
    pdf = PDFCrop(path)
