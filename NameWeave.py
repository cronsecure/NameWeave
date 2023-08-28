import argparse

def generate_username_combinations(names_lastnames):
    combinations = []

    for name, lastname in names_lastnames:
        username1 = name.lower() + lastname.lower()
        username2 = name.lower() + '.' + lastname.lower()
        username3 = name[0].lower() + '.' + lastname.lower()
        username4 = name[0].lower() + lastname.lower()
        username5 = name.lower() + '.' + lastname[0].lower()
        combinations.extend([username1, username2, username3, username4])

    return combinations

# Configurar el análisis de argumentos
parser = argparse.ArgumentParser(description='Script para generar combinaciones de nombres de usuario')
parser.add_argument('-f', '--file', metavar='FILE', required=True, help='Archivo con la lista de nombres y apellidos')

# Analizar los argumentos pasados al script
args = parser.parse_args()

# Obtener el nombre del archivo desde los argumentos
file_name = args.file

# Leer el archivo de nombres y apellidos
with open(file_name, 'r') as file:
    names_lastnames = [line.strip().split(' ') for line in file]

# Generar las combinaciones de nombres de usuario
username_combinations = generate_username_combinations(names_lastnames)

# Imprimir las combinaciones generadas
for username in username_combinations:
    print(username)
