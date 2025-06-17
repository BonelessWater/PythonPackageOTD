'''
Day 11, June 16th 2025: 

Welcome to qrcode!

Bridge the physical and digital worlds with QR codes.
From URLs to WiFi passwords, contact info to plain text -
generate scannable codes in seconds. Perfect for events,
sharing, and making life a little more convenient.
'''

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# Basic QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data('https://domdupuy.com')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('basic_qr.png')

# Styled QR code with rounded corners
qr_styled = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr_styled.add_data('Hello, QR World!')
qr_styled.make(fit=True)
styled_img = qr_styled.make_image(image_factory=StyledPilImage,
                                 module_drawer=RoundedModuleDrawer())
styled_img.save('styled_qr.png')

# WiFi QR code (scan to connect)
wifi_data = 'WIFI:T:WPA;S:MyNetwork;P:MyPassword;H:false;;'
qr_wifi = qrcode.make(wifi_data)
qr_wifi.save('wifi_qr.png')

print("QR codes generated: basic_qr.png, styled_qr.png, wifi_qr.png")