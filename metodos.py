monstruo1 = 'Genormica'
monstruo2 = 'ceNtuRioN'
monstruo3 = 'cucharacha'
monstruo4 = '   aurora y animalica'

# Todas las letras de la variable en Mayusculas
print(monstruo1.upper())
# Todas las letras de la variable en Minusculas
print(monstruo2.lower())
# Pone la primera letra de la variable en mayuscula
print(monstruo4.capitalize())
# Pone la primera letra de la variable en mayuscula + lstrip, elimina los espacios en blanco de la izq
print(monstruo4.lstrip().title())
# rstrip, elimina los espacios en blanco de la derecha
print(monstruo4.rstrip())
# Find encuentra los caracteres que proporcionemos en la busqueda, como parámetro y nos devuelve su lugar en formato array
print(monstruo4.find("mali"))  # Si resulta -1 significa que no lo encontró
# reemplaza los valores que pongamos en la variable que necesitemos
print(monstruo1.replace("mica", "micosqui"))
# in, me indica si la cadena de caracteres que pasé por parametro se encuentra en una variable y devuelve un booleano
print("mica" in monstruo1)
