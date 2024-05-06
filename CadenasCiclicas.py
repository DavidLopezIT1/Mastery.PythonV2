# En python los for son mucho más sencillos, tienen la opcion de los rangos
# ejemplo:

# (for) (numero)  # crear variable () # (in) # dentro del rango (range(NumeroX))
for numero in range(6):
    print(numero)
    print(numero*3)
    print('\n')


#for else
buscar = 15
for numero in range(12):
    print(numero)
    if numero == buscar:
        print("Se ha encontrado -> ", buscar)
        break
else:
    print("No encontré el numero que buscas", '\n')

# Estructuras ciclicas iterables como strings

for numero in 'Creatina':
    print(numero.upper())
