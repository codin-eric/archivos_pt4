"""
Coding-eric video 17
Archivos pt 4 

Leer de un archivo persona.json y pasar su contenido a una estructura de python.
Luego crear un nuevo elemento y guardarlo en un archivo json
"""

import json

with open("persona.json") as fi:
	persona = json.loads(fi.read())

"""
{'nombre': 'Bruno', 
 'apellido': 'Diaz', 
 'hobbies': [
    'escalar', 
    'base jump', 
    'batman'], 
 'hijos': [
     {'nombre': 'Helena', 'edad': 18}, 
     {'nombre': 'Damian', 'edad': 13}
     ]
}
"""

eric = {
	'nombre': "Eric",
	'edad': 27,
	'hobbies': [
		"programar",
		"jueguitos",
		"editar videos"
	],
	'hijos': None
}

with open("persona_eric.json", "w") as fo:
	json.dump(eric, fo)