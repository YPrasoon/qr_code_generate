#QR Code
#before running the code, it is recommended to use the local machine rather than on a online IDE
import qrcode

qr = qrcode.QRCode(version = 1, box_size = 5, border = 2)
data = "add the link here "    # replace the string with actual link for which the QR_code need to be generated

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'white')


img.save('add the destination folder, where you want to store the generated QR_code') # replace the string with actual path