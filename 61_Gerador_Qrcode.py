

#Url que deseja codificar no QRcode
import qrcode


url = "https://www.google.com.br"

#Criando o Objeto QRcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#Adicionando os dados ao QRCode
qr.add_data(url)
qr.make(fit=True)
#Criando uma imagem do QRCode
img = qr.make_image(fill='black', black_color='white')
#Salvando o QRCode como arquivo de imagem
img.save('qrcode_google.png')
print("QRcode para o Google gerado com sucesso!")
