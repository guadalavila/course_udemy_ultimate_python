n1 = input("Ingresa el primer número ")
n2 = input("Ingresa el segundo número ")

print(n1 + n2)

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2


mensaje = f""""
Para los números {n1} y {n2}
el rdo de la suma es {suma}.
el rdo de la resta es {resta}.
el rdo de la multiplicación es {multi}.
el rdo de la división es {divi}.
"""
print(mensaje)
