# EJERCICIO 2

# Crear un conjunto llamado usuarios con los nombres: Marcela, David, Elvira, Juan, y Marcos.
usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}
print('Usuarios:', usuarios)

# Crear un conjunto llamado administradores con los nombres: Juan y Marcela.
administradores = {"Juan", "Marcela"}
print('Administradores:', administradores)

# Eliminar a Juan del conjunto de administradores.
administradores.discard("Juan")
print('Administradores:', administradores)

# Añadir a Marcos como administrador, pero mantenerlo en el conjunto de usuarios.
administradores.add("Marcos")
print('Administradores:', administradores)


# Mostrar todos los usuarios, indicando si cada uno es administrador o no.
print('\nListado de Usuarios: \n')
for usuario in usuarios:
    if usuario in administradores:
        print(f'El usuario: {usuario} SI es un Administrador')
    else:
        print(f'El usuario: {usuario} NO es Administrador')