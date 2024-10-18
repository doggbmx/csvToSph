import pandas as pd

# Cargar el archivo CSV
csv_file_path = 'YOUR_CSV_FILE_PATH'
data = pd.read_csv(csv_file_path)

# Filtrar las columnas necesarias
coordinates = data[['Local de coleta', 'Coordenadas', 'Unnamed: 5']].dropna()
print(coordinates)
# Crear el contenido del archivo .sph
sph_content = ""
for index, row in coordinates.iterrows():
    local, lat, lon = row['Local de coleta'], row['Coordenadas'], row['Unnamed: 5']
    sph_content += f"{local}: {lat}, {lon}\n"

# Guardar el .sph
sph_file_path = './sph/coordinates.sph'
with open(sph_file_path, 'w') as file:
    file.write(sph_content)

print(f"Archivo .sph generado en: {sph_file_path}")
