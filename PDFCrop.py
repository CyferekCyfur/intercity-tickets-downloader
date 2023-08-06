import os
from pdf2image import convert_from_path
from PIL import Image


class PDFCrop:
    def __init__(self, tickets_path, qr_path):
        self.tickets_path = tickets_path
        self.qr_path = qr_path

    def get_qr_path(self):
        return self.qr_path

    def get_tickets_path(self):
        return self.tickets_path

    def get_files(self):
        return self.files

    def set_files(self, x):
        self.files = x

    def scan_for_tickets(self, path):

        file_types = ["pdf", "jpg"]

        files = os.listdir(path)
        files = [file for file in files if file.split('.')[-1] in file_types]
        return files

    def crop_jpg(self):
        files = self.scan_for_tickets(self.get_qr_path())
        for file in files:
            img = Image.open(self.get_qr_path() + file)
            area = (0, 0, 1600, 950)
            img2 = img.crop(area)
            img2.save(self.get_qr_path() + file)

    def convert(self):
        files = self.scan_for_tickets(self.get_tickets_path())
        for file in files:
            size = len(file)
            image = convert_from_path(self.get_tickets_path() + file,
                                      output_folder=self.get_qr_path(),
                                      fmt="jpg",
                                      output_file="qr_" + file[:size - 4])

        files = self.scan_for_tickets(self.get_qr_path())
        for file in files:
            os.rename(self.get_qr_path() + file,
                      (self.get_qr_path() + file).replace(file[-10:-4], ""))
