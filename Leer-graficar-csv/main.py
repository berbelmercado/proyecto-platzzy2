import utilidades as utl

opcion = input('Ingrese país: ')

COpcion = utl.manejo_strings(opcion)
grOpcion = int(
    input('Ingrese 1 para Diagrama de barracongos\nIngrese 2 para Diagramas de sectores\n'))

utl.generar_grafica_pais(COpcion, grOpcion)
