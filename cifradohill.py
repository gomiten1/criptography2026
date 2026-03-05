import numpy as np

def cifrado(mensaje, llave):
  L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  L2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
  mapeo = dict(zip(L, L2))
  mapeo2 = dict(zip(L2,L))
  m = mensaje
  k = llave   
  mensaje_convertido = [mapeo[letra] for letra in m if letra in mapeo]
  llave_convertida = [mapeo[letra] for letra in k if letra in mapeo]

  matriz_llave = np.array(llave_convertida).reshape(3,3)
  matriz_mensaje = np.array(mensaje_convertido).reshape(3,1)

  resultado = matriz_llave @ matriz_mensaje
  cifrado = resultado%26
  cifrado =cifrado.reshape(-1)

  mensaje_cifrado = ''
  arreglo_cifrado = [mapeo2[letra] for letra in cifrado if letra in mapeo2]
  print(arreglo_cifrado)
  for i in arreglo_cifrado:
    mensaje_cifrado+=i

  return cifrado, mensaje_cifrado, matriz_llave, matriz_mensaje

def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def descifrado(cifrado, matriz_llave):
  L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  L2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
  mapeo = dict(zip(L, L2))
  mapeo2 = dict(zip(L2,L))

  det = int(round(np.linalg.det(matriz_llave)))
  det_mod = det % 26

  det_inv = mod_inv(det_mod, 26)

  adjunta = np.round(det * np.linalg.inv(matriz_llave)).astype(int)

  inversa_llave = (det_inv * adjunta) % 26

  matriz_descifrada = (inversa_llave @ cifrado) % 26
  matriz_descifrada = matriz_descifrada.reshape(-1)

  arreglo_descifrado = [mapeo2[int(letra)] for letra in matriz_descifrada]

  return arreglo_descifrado, matriz_descifrada


if __name__ == "__main__":
  mensaje = input("Ingrese el mensaje a cifrar: ")
  llave = input("Ingrese la llave para el cifrado: ")
  cifrado, mensaje_cifrado, matriz_llave, matriz_mensaje = cifrado(mensaje, llave)

  print(f"Cifrado: {cifrado}")
  print(f"Mensaje cifrado: {mensaje_cifrado}")

  mensaje_descifrado, arreglo_descifrado = descifrado(cifrado, matriz_llave)
  print(f"Matriz descifrada: \n{arreglo_descifrado}")
  print(f"Mensaje descifrado: \n{mensaje_descifrado}")

  