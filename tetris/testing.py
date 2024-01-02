def letrasNumeros(textoPantalla):
    digitos = 0
    letras = 0

    for i in textoPantalla:
        if i.isdigit():
            digitos += 1
        elif i.isalpha():
            letras += 1
        else:
            pass
    return digitos, letras

a = 'abcd 1122 abcd1324 ff44 44'

#print(letrasNumeros(a))

b = letrasNumeros(a)
print('a '+ a)
print(b)
print('b '+b)
print('2: '+b[2:])
print(':2 '+b[:2])
print('1: '+b[1:])
print(':1 '+b[:1])
print(':0 '+b[:0])
print('0: '+b[0:])