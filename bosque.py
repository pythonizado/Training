import random

#guiar aventurero
#debí generar una clase pero me iba a llevar más tiempo y más logica para pasar los argumentos a cada metodo

#asigno valores a las variables segun comienza el juego
energia=100
salud = 80
experiencia =  50
nivel = 1
pocion = False
manzana = False
enemigos = ['Goblin', 'Troll']


#1
def mensaje_inicial():
    print('¡Bienvendio al Bosque Encantado! Tu aventura comienza ahora.')
    if energia>=50:
        print('Estas listo para la aventura')
    else:
        print('Necesitas más energía antes de commenzar') 

#2
def verificar_estado():
    if salud <=0:
        print('Aventurero caido')
    else:
        print('El aventurero sigue luchando')

#3
def descansar():
    global energia 
    energia = energia + 20
    print('ya descansé')
    opciones()

#4
def pelear(x):
    global enemigos
    global salud
    if enemigos[x]==0:
        salud = salud-10
        energia = energia-30
    elif enemigos[x]==1:
        salud = salud-30
        energia = energia-50
    else:
        print('el nombre ingresado de enemigo no es correcto')
    print('ya pelie')
    opciones()
#print(verificar_estado()) //no me queda claro donde debía verificar el estado

#5
def usar_objeto(ob):
    global pocion
    global manzana
    if ob == False:
        if ob == pocion:
            salud = salud+30
            pocion = True
        elif ob == manzana:
            energia = energia+10
    else:
        print('Objeto no disponible')
    print('ya usé el objeto')
    opciones()
#6
def explorar():
    global experiencia
    global nivel
    evento = random.randint(1,6)
    if evento == 3:
        pelear(enemigos[0])
    elif evento == 5:
        pelear(enemigos[1])
    else:
        if experiencia<50:
            print('Aventura superada con éxito gana 10pts en exp')
        else:
            nivel = nivel+1
            experiencia=0
            print('Aventura superada con éxito, subiste un nivel')
    print('ya exploré')
    opciones()

#pantalla inicial
#No sé como realizar saltos de línea en python
def opciones():
    global salud
    global energia
    global nivel
    global experiencia
    x =input(f'Menu de opciones \n 1 descansar \n 2 explorar \n 3 Usar objeto \n 4 estado de la partida \n 0 salir  \n Elige una opcion (1-4)\n')
    x = int(x)
    #debí usar n switch case pero no recuerdo la sintaxis en python así que fui por lo fácil
    while x!=0:
        if x==0:
            energia = 100
            salud = 80
            experiencia =  50
            nivel = 1
            exit
            break
        elif x==1:
            descansar()
            break
        elif x==2:
            explorar()
            break
        elif x==3:
            objetito = input('Ingrese un objeto: manzana (m) o pocion (p)')
            usar_objeto(objetito)
            break
        elif x==4:
            print(f'La salud del expolorador es: {salud}')
            print(f'La energia del expolorador es: {energia}')
            print(f'El nivel del expolorador es: {nivel}')
            opciones()
            break
        else:
            print('algo está fallando pibe')
            break

mensaje_inicial()
opciones()












  
        


