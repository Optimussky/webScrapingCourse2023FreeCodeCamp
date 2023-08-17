from bs4 import BeautifulSoup # Sólo para revisar
import requests
import bs4
print("Versión de BeautifulSoup:", bs4.__version__)
print("Versión de requests:", requests.__version__)


#pip install beatifulsoup==4.11.2
#pip install requests==2.27.1

# Inicio del webScraping

# 1.- Obtener el HTML
URL_BASE = "https://i4ch-capitalhumano.cdmx.gob.mx/usuario/recibo/listado?anio=2022"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

# 2.- "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido, "html.parser")

## Utilizando atributos de las etiquetas
print("""\n\n
		Utilizando atributos de las etiquetas""")
# En lugar de traer todos los h2, o en este caso todos los divs, podemos pedir...
# Los divs que contengan... una clase en específico
# Es importante notar que NO SE PUEDE usar class
# Se debe utilizar una palabra no reservada en este caso "class_" class con guión bajo

# Clase

target_i = soup.find_all('div', class_ = "content")
# También podría pedir no sólo información de un div, sino cualquier clase que contenga: ""heading-container heading-center""
# Omitiendo el div:
#divs = soup.find_all(class_ = "heading-container heading-center")
for i in target_i:
	print(i)
	print(" ")

"""

# Todas las etiquetas que contengan el atributo "src"
print('\n\nTodas las etiquetas que contengan el atributo "src" y terminen en jpg')

src_todos = soup.find_all(src=True)

for elemento in src_todos:
	if elemento['src'].endswith(".jpg"):
		print(elemento)


# Ejercicio Descargar todas la imágenes:



url_imagenes = []

for i, imagen in enumerate(src_todos):
	if imagen['src'].endswith('png'):
		print(imagen['src'])
		#r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")
		r = requests.get(f"https://scrapepark.org/spanish/{imagen['src']}")

		with open(f'imagen_{i}.png', 'wb') as f:
			f.write(r.content)
"""