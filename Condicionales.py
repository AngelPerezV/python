"""
Condicionales (pt. I)
Los condicionales los utilizaremos para validar si se cumple una o más condiciones para ejecutar cierto bloque de código, en esencia nos ayuda a tomar decisiones sobre el flujo de nuestro código.
"""
"""
Sintaxis:
if condition:
    # Block of code
elif other_condition:
    # Another block of code
else:
    # Final block of code """
edad=24
print(edad)

edad=input("Escribe tu edad:  ")
edad = int(edad)#casting 
if edad >= 18 and edad <= 100:
    print("Eres Mayor de edad: ")
elif edad > 100:
    print("ya te petataste. ")
elif edad < 0:
    print("tu edad no tiene sentido.")
else:
    print("Eres menor de edad xd. ")

richard = 27
rodo = 17
rafa = 22

edad_total = richard + rodo + rafa
print(edad_total)
print(richard)
print(rodo)
print(rafa)

if richard >= 18 and rodo >= 18 and rafa >= 18:
    print("Todos son mayores.")
else:
    print("Alguien es menor. ✖️")

#If anidados 

animal = "caballo"
color = "blanco"


if animal == "caballo":
    if color == "negro":
        print("Ah, es el caballo de Juan.")
    else:
        print("No sé de quién sea.")
else:
    print("No sé qué animal es.")

if color == "negro":
    print("Ah, es el caballo de Juan.")
else:
    print("No sé de quién sea.")

color = "negro"
"Ah, es el caballo de Juan." if color == "negro" else "No sé de quién sea."



z = 2 + 3j

print(z.__dir__())

print(z.real, z.imag)
print(z.conjugate())
