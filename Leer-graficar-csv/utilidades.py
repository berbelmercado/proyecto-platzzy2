import graficarInformacion as gr
'''importación para leer archivos'''
import read_cvs as rd


def population_by_country(data, country):
    '''retorna la información que se solicita'''
    for line in data:
        if country in line['Country Name']:
            country = line['Country Name']

    result = list(filter(lambda item: country in item['Country Name'], data)
                  )  # usamos "in" en vez de "==" para buscar concidencias y evitar errores si el nombre del país viene acompañado de otros strings
    return result, country


def manejo_strings(opcion):
    '''convierte la primera letra del string en mayusculas'''

    opcion = opcion.lower().title()
    return opcion


def year_data(pais):
    '''Optiene los datos por año y los convierte a tipo float'''
    date_year = {
        '1960': float(pais['1960']),
        '1961': float(pais['1961']),
        '1962': float(pais['1962']),
        '1963': float(pais['1963']),
        '1964': float(pais['1964']),
        '1965': float(pais['1965']),
        '1966': float(pais['1966']),
        '1967': float(pais['1967']),
        '1968': float(pais['1968']),
        '1969': float(pais['1969']),
        '1970': float(pais['1970']),
        '1971': float(pais['1971']),
        '1972': float(pais['1972']),
        '1973': float(pais['1973']),
        '1974': float(pais['1974']),
        '1975': float(pais['1975']),
        '1976': float(pais['1976']),
        '1977': float(pais['1977']),
        '1978': float(pais['1978']),
        '1979': float(pais['1979']),
        '1980': float(pais['1980']),
        '1981': float(pais['1981']),
        '1982': float(pais['1982']),
        '1983': float(pais['1983']),
        '1984': float(pais['1984']),
        '1985': float(pais['1985']),
        '1986': float(pais['1986']),
        '1987': float(pais['1987']),
        '1988': float(pais['1988']),
        '1989': float(pais['1989']),
        '1990': float(pais['1990']),
        '1991': float(pais['1991']),
        '1992': float(pais['1992']),
        '1993': float(pais['1993']),
        '1994': float(pais['1994']),
        '1995': float(pais['1995']),
        '1996': float(pais['1996']),
        '1997': float(pais['1997']),
        '1998': float(pais['1998']),
        '1999': float(pais['1999']),
        '2000': float(pais['2000']),
        '2001': float(pais['2001']),
        '2002': float(pais['2002']),
        '2003': float(pais['2003']),
        '2004': float(pais['2004']),
        '2005': float(pais['2005']),
        '2006': float(pais['2006']),
        '2007': float(pais['2007']),
        '2008': float(pais['2008']),
        '2009': float(pais['2009']),
        '2010': float(pais['2010']),
        '2011': float(pais['2011']),
        '2012': float(pais['2012']),
        '2013': float(pais['2013']),
        '2014': float(pais['2014']),
        '2015': float(pais['2015']),
        '2016': float(pais['2016']),
        '2017': float(pais['2017']),
        '2018': float(pais['2018']),
        '2019': float(pais['2019']),
        '2020': float(pais['2020']),
        '2021': float(pais['2021']),
    }
    return date_year.keys(), date_year.values()


def generar_grafica_pais(country, opcion):
    '''genera graficas de barras por pais que seleccionemos'''
    data = rd.read_cvs(
        'C:/Users/DELL/Downloads/T1.csv')
    pais, country = population_by_country(data, country)
    pais = pais[0]
    year, dato = list(year_data(pais))

    if opcion == 1:
        gr.generar_imagen_barras(year, dato, country)
    elif opcion == 2:
        gr.generar_imagen_circulo(year, dato, country)
