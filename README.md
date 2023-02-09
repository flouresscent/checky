# Checky

Checky is a service for people who like to keep track of their money spending. Now only the first version of the algorithm is presented here, but in the future it is planned to release a telegram bot and a user application.

## Usage Guide
Firstly place the photo of the receipt with the qr-code in the tests folder and change the path to the photo in the file decode_qr.py
```python
  PATH_TO_QR = "tests/PHOTO_OF_YOUR_RECEIPT.jpg"
```

Next, run the file main.py . In the field that appears, enter your phone number, and then enter the SMS confirmation code that will be sent to the specified number.
```
  [PHONE] Enter the phone number in the format +7XXXXXXXXXX: +71234567890
  [CODE] Enter the code from the SMS: 1234
```

After the program is completed, a json file with information about the receipt and purchases will be available in the receipts folder in the format:
```
  /receipts/YYYY-MM-DDTHH-MM-SS.json
```

## Development plans
Now the main task is to write a custom application that will simplify the use of the algorithm, and processing a json file containing information about the purchase.

###### So far, it only works in the RU region
