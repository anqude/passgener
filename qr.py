import qrcode
def generate_qr(password):
    qr = qrcode.QRCode()
    qr.add_data('password: '+password)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save("qr.png")
