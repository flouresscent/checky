import json
import re
import dateutil.parser

from decode_qr import DecodeQR
from receipt_processing import ReceiptProcessing

if __name__ == '__main__':
    decode_qr = DecodeQR()
    decoded_info = decode_qr.decode_qr_code()
    # print(decoded_info)

    t = re.findall(r't=(\w+)', decoded_info)[0]
    datetime = dateutil.parser.isoparse(t)
    datetime = str(datetime).replace(" ", "T")
    datetime = str(datetime).replace(":", "-")

    client = ReceiptProcessing()
    ticket = client.get_ticket(decoded_info)
    ticket = json.dumps(ticket, indent = 4, ensure_ascii = False)
    # print(ticket)
    with open(f'receipts/{datetime}.json', 'w', encoding='utf-8') as res_data:
        res_data.write(ticket)