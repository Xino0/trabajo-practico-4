# EJERCICIO 1

numerosEnteros = list(range(9))

while True:
    vPorTeclado = int(input('Ingrese un valor del 0 al 9: '))
    if(vPorTeclado in numerosEnteros):
        print(f'El numero {vPorTeclado} SI esta en la lista')
        break
    else:
        print(f'El numero {vPorTeclado} NO esta en la lista')