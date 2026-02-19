def cifrar(mensaje: str, llave: str) -> str:
    """Cifra un mensaje utilizando el cifrado Vigenere."""
    
    resultado = ""
    index = 0
    for caracter in mensaje:
        if caracter == " ":
            resultado += " "
        elif not caracter.isalpha():
            resultado += caracter
        elif caracter.isupper():
            resultado += chr(((ord(caracter) - ord('A')) + ord(llave[index]) - ord('A')) % 26 + ord('A'))
        else:
            resultado += chr((ord(caracter) - ord('a') + ord(llave[index]) - ord('a')) % 26 + ord('a'))
        index += 1
    return resultado

def descifrar(mensaje: str, llave: str) -> str:
    """Descifra un mensaje utilizando el cifrado Vigenere."""
    
    resultado = ""
    index = 0
    for caracter in mensaje:
        if caracter == " ":
            resultado += " "
        elif not caracter.isalpha():
            resultado += caracter
        elif caracter.isupper():
            resultado += chr((ord(caracter) - ord('A') - ord(llave[index]) + ord('A')) % 26 + ord('A'))
        else:
            resultado += chr((ord(caracter) - ord('a') - ord(llave[index]) + ord('a')) % 26 + ord('a'))
        index += 1
    return resultado

def generarLlave(mensaje: str, clavePreeliminar: str) -> str:
    """Genera una llave para el cifrado Vigenere
    la llave se repite hasta alcanzar la longitud del mensaje"""
    llave = ""
    index = 0
    for caracter in mensaje:
        if caracter == " ":
            llave += " "
        else:
            llave += clavePreeliminar[index % len(clavePreeliminar)]
            index += 1
    return llave

if __name__ == "__main__":
    mensaje = input("Ingrese el mensaje a cifrar: ")
    clave = input("Ingrese la clave para el cifrado: ")
    llave = generarLlave(mensaje, clave)
    print(f"Llave generada: {llave}")
    mensaje_cifrado = cifrar(mensaje, llave)
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    mensaje_descifrado = descifrar(mensaje_cifrado, llave)
    print(f"Mensaje descifrado: {mensaje_descifrado}")