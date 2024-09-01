#mision 1
objetos =['Sable de luz', 'Holocron', 'Mapa estelar']
print(objetos)
#test case 1 valor valido: 'Sable de luz', 'Holocrón', 'Mapa estelar' 
agregando = input('agregue un elemento brother')
objetos.append(agregando)
print(f'test case 2 {objetos}')
#test case 2 valor valido: 'Sable de luz', 'Holocrón', 'Mapa estelar', agregando

#mision 2
print(f'test case 3 {objetos[0], objetos[-1]}')
#test case 3 valor valido: 'Sable de luz',agregado

#mision 3
agregandoUnaVezMas = input('agregue un elemento a la lista guachin')
objetos[1]=agregandoUnaVezMas
print(f'test case 4{objetos}')
#test case 4 valor valido: 'Sable de luz', agregandoUnaVezMas, 'Mapa estelar', agregando

#mision 4
objetos.insert(1,'algo nuevo')
print(f'test case 5 {objetos}')
#test case 5 valor valido:'Sable de luz', 'algo nuevo', agregandoUnaVezMas, 'Mapa estelar', agregando
eliminame = input('ingrese el elemeto a eliminar pero escribilo bien al nombre sino no funciona pibe')
objetos.remove(eliminame)
print(f'test case 6 {objetos}')
#test case 6 valor valido para input 'algo nuevo':'Sable de luz', agregandoUnaVezMas, 'Mapa estelar', agregando
soyPop = objetos.pop(-1)
print(f'test case 7 {soyPop}')
#test case 7 valor valido: agregado

#mision 5
herramientas =['Desarmador', 'llave inglesa', 'martillo']
inventario = objetos+herramientas
print(f'test case 8 {inventario}')
#test case 8 valor valido:['Sable de luz', 'algo nuevo', agregandoUnaVezMas, 'Mapa estelar']['Desarmador', 'llave inglesa', 'martillo']
print(len(f'test case 9 {inventario}'))
#test case 9 valor valido: 7
print('test case 10: ')
print('Sabele de luz' in inventario)
#test case 10 valor valido: True

#mision 6
inventario.sort
print(f'test case 11 {inventario}')
#test case 11 valor valido:[agregandoUnaVezMas,'algo nuevo','Mapa estelar','Sable de luz']['Desarmador', 'llave inglesa', 'martillo']
inventario.reverse
print(f'test case 12 {inventario}')
#test case 12 valor valido:[agregandoUnaVezMas,'algo nuevo','Mapa estelar','Sable de luz']['Desarmador', 'llave inglesa', 'martillo'] pero al reves jaja
indexMapa = inventario.index('Mapa estelar')
print(f'test case 13 {indexMapa}')
#test case 13 valor valido: -3
contandoHolocron = inventario.count('Holocron')
print(f'test case 14 {contandoHolocron}')
#test case 14 valor valido: 1

#mision 7
poderes=[50,70,85,60,90]
print(f'test case 15 {max(poderes)}')
#test case 15 valor valido: 90
print(f'test case 16 {min(poderes)}')
#test case 16 valor valido: 50
print(f'test case 17 {sum(poderes)}')
#test case 17 valor valido: 355
print(f'test case 18 {len(poderes)}')
#test case 18 valor valido: 5











