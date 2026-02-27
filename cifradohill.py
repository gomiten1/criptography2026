import numpy as np

L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
mapeo = dict(zip(L, L2))
mapeo2 = dict(zip(L2,L))
m = 'act'
k = 'gybnqkurp'
mensaje_convertido = [mapeo[letra] for letra in m if letra in mapeo]
llave_convertida = [mapeo[letra] for letra in k if letra in mapeo]

matriz_llave = np.array(llave_convertida).reshape(3,3)
matriz_mensaje = np.array(mensaje_convertido).reshape(3,1)

resultado = matriz_llave @ matriz_mensaje
cifrado = resultado%26
cifrado =cifrado.reshape(-1)
print(cifrado)

mensaje_cifrado = ''
arreglo_cifrado = [mapeo2[letra] for letra in cifrado if letra in mapeo2]
for i in arreglo_cifrado:
  mensaje_cifrado+=i

print(mensaje_cifrado)