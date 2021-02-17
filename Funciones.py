"""
Funciones (pt. I)
La manera en la que empaquetamos procesos que ejecutan un bloque completo de código es a través de funciones, la sintaxis de Python es muy sencilla y eficiente para escribir bloques de código de forma ordenada.

La mayoría de los paquetes en Python están conformados por objetos y funciones.

Sintaxis:
def function_name(arguments):
    # Block of code
    # Final block of code
    return something
"""
taquerias = [
    "Los Güeros",       # 0 La pocision en que se encuantra el elemento en la lista 
    "Veloz",            # 1
    "Tacos Los Papis",  # 2
    "Takesabroso",      # 3
    "Takos El Rodo"     # 4
]

def F(masa):
    #segunda ley de Newton
    #F = masa * acelaracion 
    a=9.81
    print (masa*a)
F(80)
F(56)
F(67)
#Otra forma de hacerlo es 
def F(masa):
    #segunda ley de Newton
    #F = masa * acelaracion 
    a=9.81
    Fuerza = masa*a
    print (Fuerza)
F(80)
F(56)
F(67)
def segunda_de_newton(masa, acelaracion):
    fuerza=masa*acelaracion
    return fuerza
print("fuerza e la tierra")
print(segunda_de_newton(50,9.81))
print("Fuerza en la Luna:")
print(segunda_de_newton(50, 1.62))

def segunda_de_Newton(masa, aceleracion, nombre_del_ente="planeta"):
    fuerza = masa * aceleracion
    return -fuerza
print("Fuerza en la Tierra:")
print(segunda_de_Newton(50, 9.81))

print("Fuerza en la Luna:")
print(segunda_de_Newton(50, 1.62))

#Variables globales y locales 
def F(masa, acel):
    global taquerias#la palabra global para dar acceso a una variable local 
    taquerias.append("Luna")
    f = masa*acel
    return f
F(50, 9.81)
print(taquerias)
