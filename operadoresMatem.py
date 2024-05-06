import math

numero1 = 1 + 7
numero2 = 2 - 1
numero3 = 30 / 3
numero4 = 4.3
numero4 += 4.9
print(numero1 // numero4)

# Nos devuelve lo que sobra de una division
print(3 % 9)
# Nos eleva a la potencia un numero o expresion matematica
print(98**2)
# la expresion += nos suma o agrega el valor de una variable nueva al numero de la variable como se ve en el ejemplo
print(numero4)

# Funciones nativas
# Nos devuelve el entero al que esté mas cercano
print(round(1.9))
print(round(1.5))
print(round(1.7))
print(round(1.3))
# Nos genera numeros absolutos
print(abs(-1.9))
print(abs(-1.5))
print(abs(-1.7))
print(abs(-1.3))

# Funciones de Import math
# Superior entero mas cercano
print(math.ceil(1.9))
# Inferior entero mas cercano
print(math.floor(-1.5))
# devuelve un booleano de si es o no un numero
print(math.isnan(7))
# Potencia del numero
print(math.pow(1.3, 4))
# raiz cuadrada del numero parametrizado
print(math.sqrt(36))
