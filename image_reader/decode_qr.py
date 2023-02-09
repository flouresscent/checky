from pyzbar.pyzbar import decode
from PIL import Image

class DecodeQR:
    PATH_TO_QR = 'tests/test2.jpg'

    def decode_qr_code(self):
        decode_msg = decode(Image.open(self.PATH_TO_QR))
        return decode_msg[0].data.decode('ascii')

