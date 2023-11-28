import matplotlib.pyplot as plt


def generar_imagen_barras(eje_x, eje_y, country):
    '''Diagramas de barras verticales'''
    fig, ax = plt.subplots()
    ax.bar(eje_x, eje_y)
    ax.set_title(country, loc="left", fontdict={
                 'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.show()


def generar_imagen_circulo(eje_x, eje_y, country):
    '''Diagramas de sectores'''
    fig, ax = plt.subplots()
    ax.pie(eje_y, labels=eje_x)
    ax.set_title(country, loc="left", fontdict={
        'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.show()


if __name__ == '__main__':
    pais = 'Congo'
    # eje_x = ['a', 'b', 'c']
    eje_x = [
        '1970 Population',
        '1980 Population',
        '1990 Population',
        '2000 Population',
        '2010 Population',
        '2015 Population',
        '2020 Population',
        '2022 Population'
    ]
    # eje_y = [100, 10, 300]
    eje_y = [41128771, 38972230, 33753499, 28189672,
             19542982, 10694796, 12486631, 10752971]
    generar_imagen_barras(eje_x, eje_y, pais)

    # generar_imagen_circulo(eje_x, eje_y, pais)
