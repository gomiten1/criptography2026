# Programa para encontrar el inverso multiplicativo modular de un número
# De la forma n ⋅ x ≡ 1 (mod m), x es el inverso multiplicativo
# Para que exista m y n deben ser coprimos
# Se usa el algoritmo de Euclides extendido para encontrar el inverso multiplicativo

# Verificar si dos números son coprimos -> gcd(a, b) == 1
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Algoritmo de Euclides extendido para encontrar el inverso multiplicativo
def extended_euclides(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclides(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


# Obtención de inverso
def multiplicative_inverse(n, m):
    gcd, x, _ = extended_euclides(n, m)
    return x % m

# Flujo principal
if __name__ == "__main__":
    print("Encuentra el inverso multiplicativo de n módulo m")
    print("La forma es nx == 1 (mod m)")
    a = int(input("Ingrese el número n: "))
    m = int(input("Ingrese el módulo m: "))
    
    if gcd(a, m) != 1:
        print(f"No existe el inverso multiplicativo de {a} módulo {m} porque no son coprimos")
    else:
        inverse = multiplicative_inverse(a, m)
        print(f"El inverso multiplicativo de {a} módulo {m} es: {inverse}")
        print(f"Existen más de la forma")
        print(f"{a} + {inverse}k, donde k es un entero")
    