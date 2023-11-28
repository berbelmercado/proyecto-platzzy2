import csv


def read_cvs(path):
    '''Permite leer el archivo'''
    with open(path, 'r') as cvsfile:
        file = csv.reader(cvsfile, delimiter=',')
        cabecera = next(file)  # la  primera columna del archivo no es válida
        cabecera = next(file)
        # print(cabecera)
        data = []
        for line in file:
            # optenemos pares de datos----cabecera y dato al que corresponde
            # juntamos cabecera y linea leida
            tupla = list(zip(cabecera, line))
            diccionario = dict(tupla)
            data.append(diccionario)
    return (data)


if __name__ == '__main__':
    print('main')
    datos = read_cvs('C:/Users/DELL/Downloads/T1.csv')
    print(datos)
