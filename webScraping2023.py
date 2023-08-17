#webScraping2023.py

# Versiones
from bs4 import BeautifulSoup # Sólo para revisar
import requests
import bs4
print("Versión de BeautifulSoup:", bs4.__version__)
print("Versión de requests:", requests.__version__)

#pip install beatifulsoup==4.11.2
#pip install requests==2.27.1

# Inicio del webScraping

# 1.- Obtener el HTML
URL_BASE = "https://scrapepark.org/spanish/"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

# 2.- "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido, "html.parser")

# El método find(): nos permite quedarnos con la información asociada a una etiqueta de HTML
primer_h2 = soup.find('h2')
print(primer_h2)

# Sólo texto
print("""\n\n
		Sólo texto""")
print(primer_h2.text)
# Equivalente a 
#print(soup.h2.text)

# El método Find All: find_all()
# Busca todos los elementos de la página con esa etiqueta y devuleve una lista que los contiene
#(En realidad devuelve un objeto de la clase bs4.element.ResultSet)
h2_todos = soup.find_all('h2')
print("""\n\n
		Todos los h2""")
print("""\n\n
		Devuelve una LISTA DE los h2""")
print(h2_todos)

# ARGUMENTOS
# Si usamos el parámetro limit = 1, emulamos al método "find"
h2_uno_solo = soup.find_all('h2', limit=1)
print("""\n\n
		Un sólo h2""")
print(h2_uno_solo)

# También podemos iterar sobre el objeto
print("""\n\n
		También podemos iterar sobre el objeto""")
for seccion in h2_todos:
	print(seccion.text)

## Usar get_text() para tener más funcionalidades
print("""\n\n
		Usar get_text() para tener más funcionalidades")
		En este ejemplo gracias a get_text podemos limpiar espacios en blanco con strip=True""")
for seccion in h2_todos:
	print(seccion.get_text(strip=True))


## Utilizando atributos de las etiquetas
print("""\n\n
		Utilizando atributos de las etiquetas""")
# En lugar de traer todos los h2, o en este caso todos los divs, podemos pedir...
# Los divs que contengan... una clase en específico
# Es importante notar que NO SE PUEDE usar class
# Se debe utilizar una palabra no reservada en este caso "class_" class con guión bajo

# Clase

divs = soup.find_all('div', class_ = "heading-container heading-center")
# También podría pedir no sólo información de un div, sino cualquier clase que contenga: ""heading-container heading-center""
# Omitiendo el div:
#divs = soup.find_all(class_ = "heading-container heading-center")
for div in divs:
	print(div)
	print(" ")


# Todas las etiquetas que contengan el atributo "src"
print('\n\nTodas las etiquetas que contengan el atributo "src" y terminen en jpg')

src_todos = soup.find_all(src=True)

for elemento in src_todos:
	if elemento['src'].endswith(".jpg"):
		print(elemento)


# Ejercicio Descargar todas la imágenes:

print("""
		\n Ejercicio bajar todas las imágenes:\n
	""")

url_imagenes = []

for i, imagen in enumerate(src_todos):
	if imagen['src'].endswith('png'):
		print(imagen['src'])
		#r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")
		r = requests.get(f"https://scrapepark.org/spanish/{imagen['src']}")

		with open(f'imagen_{i}.png', 'wb') as f:
			f.write(r.content)
