import qrcode

# Dados que você deseja armazenar no QR Code
dados = "https://www.exemplo.com"

# Crie um objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR Code (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro (L, M, Q, H)
    box_size=10,  # Tamanho dos blocos
    border=4,  # Tamanho da borda
)

# Adicione os dados ao objeto QRCode
qr.add_data(dados)
qr.make(fit=True)

# Crie uma imagem do QR Code usando a biblioteca Pillow (PIL)
img = qr.make_image(fill_color="black", back_color="white")

# Salve a imagem ou exiba-a
img.save("qrcode.png")
img.show()
