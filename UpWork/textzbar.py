import pyzxing

def decode_qr_code(image_path):
    reader = pyzxing.BarCodeReader()
    result = reader.decode(image_path)
    print(result)

# Example usage
decode_qr_code('/Users/ionbota/Documents/Screenshot 2024-06-11 at 4.30.08 PM.png')
