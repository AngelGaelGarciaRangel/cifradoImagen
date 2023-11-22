import re

def esImagen(url):
  patron = r'\.png$|\.jpg$|\.jpeg$'
  esImagen = coincidencia = re.search(patron, url, re.IGNORECASE)
  return bool(esImagen)

def encriptar_desencriptar(url, llave):
    archivoLeer = open(url, 'rb')
    imagen = archivoLeer.read()
    archivoLeer.close()
    imagen = bytearray(imagen)
    for indice, valor in enumerate(imagen):
        imagen[indice] = valor ^ llave
    archivoLeer = open(url, 'wb')
    archivoLeer.write(imagen)
    archivoLeer.close()
    print('Hecho...')
    
def menu():
  opcion = int(input("1. Encriptar una imagen\n2. Desencriptar una Imagen\nSelecciona una opción (1 o 2): "))
  url = input("Ingresa la url de la imagen: ")
  if esImagen(url):
    try:
      llave = int(input("Ingresa la llave (debe ser la misma para encriptar y desencriptar): "))
      if opcion == 1:
        print("El url original es", url)
        print("La llave de encriptación es", llave)
        encriptar_desencriptar(url, llave)
      elif opcion == 2:
        print("El url  es", url)
        print("La llave de encriptación es", llave)
        encriptar_desencriptar(url, llave)
      else:
        print("No elegiste una opción correcta (1 o 2)")
    except:
      print("La llave que introdujiste no tuvo el formato correcto, es posible que introdujeras texto en lugar de un número entero.")
  else:
    print("El archivo que introdujiste no se trata de una imagen.")


menu()
    

#Referencias: Patil, R. (2022). Encrypt and Decrypt Image using Python. Geeksforgeeks. Recuperado de: https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/ 