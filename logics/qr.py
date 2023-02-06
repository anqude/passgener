import qrcode
def generate_qr(password,fg_color,bg_color):
    qr = qrcode.QRCode()
    qr.add_data('password: '+password)
    try:
        qr.make(fit=True)
    except:
        return False
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save("qr.png")
    return True

def generate_qr_text(password):
    qr = qrcode.QRCode()
    qr.add_data('password: '+password)
    return(qr.print_ascii())