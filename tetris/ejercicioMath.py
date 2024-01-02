from math import e, pi

a = 123.8
print('valor de a: ', a)
print ('valor original de pi: ', pi )
print('el valor de pi es: {:+.5f}'.format(pi))


#{:+} me da el signo positivo o negativo de un número
#.5f dice cuantos digitos quiero después de la coma
#esto solo sirve para las constantes obtenidas de la librería math
print('valor original de e :', -e )
print('e con signo: {:+.3f}'.format(e*-1))