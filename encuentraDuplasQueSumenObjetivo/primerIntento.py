#Con ayuda de un vecino mi madre mató un cochino

def busqueda (numbers: list, target: int) -> list:
    def busqueda_suma(start:int, target:int, combination:list):


        #si el target es 0 agrego combination a result  
        if target == 0:
            Result.append(combination[:])
            return
        #si el target es menor que 0 si el largo es es igual a 0, empiezo de nuevo
        if target < 0 or start == len(numbers): 
            return
        #index toma los valores del rango que va de 0 hasta el largo de la lista numbers
        for index in range (start, len(numbers)):
            if index > start and numbers [index] ==numbers[index-1]:
                continue
            #agrego el numero de la lista numbers en la posición de index a combination
            combination.append(numbers[index])
            #index suma 1 para recorrer todas las posición posibles, al target le resto el valor de numbers en el index y le paso la combination 
            busqueda_suma(index + 1, target - numbers[index], combination)
            #limpio la combination
            combination.pop()
    #ordeno los valores
    numbers.sort()
    #defino que result es una lista
    Result = []
    #paso los valores a la funcion con back-traking
    busqueda_suma(0, target , [] )
    #retorno a result
    return Result
#le paso una lista y un target a busqueda
print(busqueda([1,2,3,5], 6))   

