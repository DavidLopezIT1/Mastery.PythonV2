input1 = input("Ingresa el primer número -> ")
input2 = input("Ingresa el segundo número -> ")
input1 = int(input1)
input2 = int(input2)

# print(input1 + input2)

suma = input1 + input2
resta = input1 - input2
multi = input1 * input2
div = input1 / input2


mensaje = f"""
Los resultados de las operaciones de {input1} y {input2} son: \n
resultado de la suma, {suma} \n.
resultado de la resta, {resta} \n.
resultado de la multiplicacion, {multi} \n.
resultado de la division {div}.
"""

print(mensaje)
