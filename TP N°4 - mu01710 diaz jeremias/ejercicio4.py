# EJERCICIO 4

# La fábrica tiene una lista de sucursales, cada una con su nombre y una lista de instrumentos a la venta.
# De cada instrumento se conoce el ID alfanumérico, precio y tipo (Percusión, Viento o Cuerda).
sucursales = [
    {'nombre': 'norte', 'instrumentos' : [
        {'id': '1a', 'precio': 1200, 'tipo': 'percusion'},
        {'id': '1b', 'precio': 800, 'tipo': 'viento'},
        {'id': '1c', 'precio': 500, 'tipo': 'cuerda'},
    ]}, 
    {'nombre': 'sur', 'instrumentos' : [
        {'id': '2a', 'precio': 1500, 'tipo': 'percusion'},
        {'id': '2b', 'precio': 600, 'tipo': 'cuerda'},
    ]}, 
    {'nombre': 'este', 'instrumentos' : [
        {'id': '3a', 'precio': 900, 'tipo': 'viento'},
        {'id': '3b', 'precio': 700, 'tipo': 'cuerda'},
    ]}, 
    {'nombre': 'oeste', 'instrumentos' : [
        {'id': '4a', 'precio': 1300, 'tipo': 'percusion'},
        {'id': '4b', 'precio': 950, 'tipo': 'viento'},
    ]} 
]
# Método listarInstrumentos(): Mostrar todos los datos de cada instrumento en la consola.
def listarInstrumentos():
    print('--- Metodo Listar Instrumentos ---')
    for sucursal in sucursales:
        print(f'Sucursal: {sucursal['nombre']}')
        for instrumento in sucursal['instrumentos']:
            print(f'ID: {instrumento['id']}, Precio: {instrumento['precio']}, Tipo: {instrumento['tipo']}')
        print()
#listarInstrumentos()

# Método instrumentosPorTipo(tipo): Devolver una lista de instrumentos cuyo tipo coincida con el parámetro tipo.
def instrumentosPorTipo(tipo):
    print('--- Metodo Mostrar por Tipo de Instrumentos ---')
    print(f'\nInstrumento a buscar: {tipo} \n')
    for sucursal in sucursales:
        print(f'Sucursal: {sucursal['nombre']}')
        for instrumento in sucursal['instrumentos']:
            if instrumento['tipo'] == tipo:
                print(f'ID: {instrumento['id']}, Precio: {instrumento['precio']}, Tipo: {instrumento['tipo']}')
                print()
#instrumentosPorTipo('viento')

# Método borrarInstrumento(id): Recibir un ID y eliminar el instrumento asociado de la sucursal correspondiente.
def borrarInstrumento(id):
    print('--- Metodo Borrar Instrumento ---')
    print(f'\nInstrumento a eliminar: {id} \n')
    for sucursal in sucursales:
        for instrumento in sucursal['instrumentos']:
            if instrumento['id'] == id:
                print(f'Sucursal: {sucursal['nombre']}')
                sucursal['instrumentos'].remove(instrumento)
                print(f'Instrumento con ID: "{id}" ha sido eliminado\n')
                return
    print(f'ID: "{id}" no encontrado\n')
#borrarInstrumento('1f')
#borrarInstrumento('1a')

# Método porcInstrumentosPorTipo(sucursal): Recibir el nombre de una sucursal y retornar los porcentajes de instrumentos por tipo.
def porcInstrumentosPorTipo(nombre_sucursal):
    print('--- Metodo Porcentaje de Instrumentos ---')
    print(f'\nSucursal: {nombre_sucursal} \n')
    for sucursal in sucursales:
        if sucursal['nombre'].lower() == nombre_sucursal.lower():
            total = len(sucursal['instrumentos'])
            if total == 0:
                print(f"No hay instrumentos en la sucursal {nombre_sucursal}.\n")
                return
            
            tipos_contador = {'percusion': 0, 'viento': 0, 'cuerda': 0}
            for instrumento in sucursal['instrumentos']:
                tipos_contador[instrumento['tipo']] += 1
            
            for tipo, cantidad in tipos_contador.items():
                porcentaje = (cantidad / total) * 100
                print(f"Tipo: {tipo}, Porcentaje: {porcentaje:.2f}%")
            return
    print(f"No se encontró la sucursal con el nombre {nombre_sucursal}.\n")

#porcInstrumentosPorTipo('nor')

#porcInstrumentosPorTipo('norte')
#porcInstrumentosPorTipo('sur')