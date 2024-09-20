# EJERCICIO 3

usuarios = []

while True:
# Solicitar al usuario que ingrese los siguientes datos: nombre, edad, dirección y teléfono.
    nombre = str(input('Ingrese un nombre: '))
    edad = int(input('Ingrese una edad: '))
    direccion = str(input('Ingrese una direccion: '))
    telefono = int(input('Ingrese un telefono: '))

# Almacenar los datos en un diccionario llamado usuario_info.
    usuario_info = {
        'nombre' : nombre,
        'edad' : edad,
        'direccion' : direccion,
        'telefono' : telefono  
    }
    usuarios.append(usuario_info)
    
# Permitir el ingreso de información para varios usuarios.
    continuar = str(input('Desea agregar mas usuarios? S/N: '))
    if continuar.lower() != 's':
        break
# Mostrar la información ingresada para cada usuario en formato clave-valor
for i, usuario in enumerate(usuarios, 1):
    print(f"\nUsuario {i}:")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Dirección: {usuario['direccion']}")
    print(f"Teléfono: {usuario['telefono']}")