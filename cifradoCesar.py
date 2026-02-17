def cesar(mensaje: str, k: int) -> str:
    """Cifra un mensaje utilizando el cifrado César.
    Devuelve un mensaje en minúsculas, con espacios y sin caracteres especiales."""
    
    resultado = ""
    for caracter in mensaje:
        if caracter == " ":
            resultado += " "
        elif not caracter.isalpha():
            resultado += caracter
        elif caracter.isupper():
            resultado += chr((ord(caracter) - ord('A') + k) % 26 + ord('A'))
        else:
            resultado += chr((ord(caracter) - ord('a') + k) % 26 + ord('a'))
    return resultado

if __name__ == "__main__":
    mensaje = input("Ingrese el mensaje a cifrar: ")
    k = int(input("Ingrese el número de posiciones para el desplazamiento: "))
    mensaje_cifrado = cesar(mensaje, k)
    print(f"Mensaje cifrado: {mensaje_cifrado}")