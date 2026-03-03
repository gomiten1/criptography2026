import string


def GenMatrix(keyword):

    alphabet = dict()
    matrix = []

    for i in range(26):
        alphabet.update({chr(i + 97): 0})
        keyword = keyword + chr(i + 97)

    index = 0
    for c in keyword:
        if alphabet[c] == 0:
            if c == "j":
                alphabet[c] = 1
                c = "i"
                keyword = keyword[:index] + c + keyword[index:]
                continue

            alphabet[c] = 1

            if index % 5 == 0:
                matrix.append([])

            matrix[-1].append(c)
            index = index + 1

    index = 0
    for row in matrix:
        for c in row:
            alphabet[c] = (index % 5, index // 5)
            index = index + 1

    return alphabet, matrix


def FormatMessage(message):

    message = "".join(c for c in message if c not in string.whitespace)

    if len(message) % 2 != 0:
        message = message + "x"

    fmessage = []

    for i in range(0, len(message), 2):
        a = message[i]
        b = message[i + 1]

        if a == "j":
            a = i
        if b == "j":
            b = i
        if a == b:
            b = "x"

        fmessage.append([a, b])

    return fmessage


def PlayfairCypher(alphabet, matrix, message):

    cmessage = ""

    for digraph in message:
        a = digraph[0]
        b = digraph[1]

        # print(f"{a}, {b} ---> ", end="")
        # print(f"({alphabet[a][0]}, {alphabet[a][1]}), ({alphabet[b][0]}, {alphabet[b][1]}) ---> ", end="")

        if alphabet[a][0] == alphabet[b][0]:
            a = matrix[(alphabet[a][1] + 1) % 5][alphabet[a][0]]
            b = matrix[(alphabet[b][1] + 1) % 5][alphabet[b][0]]
        elif alphabet[a][1] == alphabet[b][1]:
            a = matrix[alphabet[a][1]][(alphabet[a][0] + 1) % 5]
            b = matrix[alphabet[b][1]][(alphabet[b][0] + 1) % 5]
        else:
            aux = matrix[alphabet[a][1]][alphabet[b][0]]
            b = matrix[alphabet[b][1]][alphabet[a][0]]
            a = aux

        # print(f"{a}, {b}")

        cmessage = cmessage + a + b

    return cmessage


keyword = input("Ingrese la palabra clave: ").lower()
message = input("Ingrese el mensaje: ").lower()

alphabet, matrix = GenMatrix(keyword)
message = FormatMessage(message)
cmessage = PlayfairCypher(alphabet, matrix, message)

print(f"El mensaje cifrado es: {cmessage}")

