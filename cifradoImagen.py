def encriptar(url, llave, archivo):
  print("El url original es", url)
  print("La llave de encriptación es", llave)
  archivoLeer = open(url, 'rb')
  imagen = archivoLeer.read()
  archivoLeer.close()
  imagen = bytearray(imagen)
  for indice, valor in enumerate(imagen):
	  imagen[indice] = valor ^ llave
  archivoLeer = open(url, 'wb')
  fin.write(image)
	fin.close()
	print('Encryption Done...')
 
#Referencias: Patil, R. (2022). Encrypt and Decrypt Image using Python. Geeksforgeeks. Recuperado de: https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/ 