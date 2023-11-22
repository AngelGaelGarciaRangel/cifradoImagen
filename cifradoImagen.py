def encriptar(url, llave):
    print("El url original es", url)
    print("La llave de encriptación es", llave)
    archivoLeer = open(url, 'rb')
    imagen = archivoLeer.read()
    archivoLeer.close()
    imagen = bytearray(imagen)
    for indice, valor in enumerate(imagen):
        imagen[indice] = valor ^ llave
    archivoLeer = open(url, 'wb')
    archivoLeer.write(imagen)
    archivoLeer.close()
    print('Encryption Done...')

def desencriptar(url, llave):
  print("El url original es", url)
  print("La llave de desencriptación es", llave)
  archivoLeer = open(url, 'rb')
  imagen = archivoLeer.read()
  archivoLeer.close()
  imagen = bytearray(imagen)
  for indice, valor in enumerate(imagen):
        imagen[indice] = valor ^ llave
  archivoLeer = open(url, 'wb')
  archivoLeer.write(imagen)
  archivoLeer.close()
  print('Decryption Done...')
url = input("Ingresa el url de la imagen: ")
llave = int(input("Ingresa la llave:"))
desencriptar(url, llave)

#Referencias: Patil, R. (2022). Encrypt and Decrypt Image using Python. Geeksforgeeks. Recuperado de: https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/ 