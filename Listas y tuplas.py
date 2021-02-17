import numpy as np 
#Repaso 
nombre= "rodolfo "
edad = 27
pi = 3.14159265358979
print()

if edad >= 18:
    print("eres mayor de edad ")
""" Listas y tuplas
Una colección es un conjunto de elementos que se agrupan en una sola estructura de datos de Python.
De manera nativa Python tiene soporte para:

Listas y tuplas
Diccionarios y conjuntos
¿Otros? """

my_list = [1.0,2.0,3.0]
my_tuple = (1.0,2.0,3.0)
my_dic = {
    "day":6,
    "month": "august "
}
""" 
*Las listas y tuplas tienen un índice asociado.
*Las listas y tuplas tienen una longitud (número de elementos) asociado.
*Se puede hacer slicing.
"""
#Creamos una lista que se llame Taquerias, se puede escribir en una sola linea de codigo ejemplo 
#taquerias =["Los guereos","veloz".....]
taquerias = [
    "Los Güeros",       # 0 La pocision en que se encuantra el elemento en la lista 
    "Veloz",            # 1
    "Tacos Los Papis",  # 2
    "Takesabroso",      # 3
    "Takos El Rodo"     # 4
]

print(taquerias)
#Ha esto se le llama indexacion o acceder a valores de una lista atraves de indices 
print(taquerias[0])
print(taquerias[3])
#como saber la longitud de una lista 
#length 
print(len(taquerias))
#manejar indices nos permitira acceder a los elementos y modificarlos 
print(taquerias[0])
taquerias[0]="El guero "
print(taquerias[0])

#tuplas: una tupla es como una lista solo que en lugar de utilizar corchetes , se utiliza parentesis 
taquerias_t = (
    "Los Güeros",       # 0 La pocision en que se encuantra el elemento en la tupla 
    "Veloz",            # 1
    "Tacos Los Papis",  # 2
    "Takesabroso",      # 3
    "Takos El Rodo"     # 4
)

#si quiero acceder a una tupla es lo mismo que en el de la lista  Ejemplo:
print(taquerias_t[0])
#solo que una vez creada una tupla sus datos no se pueden cambiar de la misma manera que los de una lista 
#las tuplas son inmutables (no cambia)

#La indexacion 
# entre corchetes podemos especificar el  indice de inicio y de fin -1 y el tamaño de salto 
#lo que signfica que podemos saltarnos de 1 en 1 o en pares. EJEMPLO :

# [inicio:fin - 1:salto] <-- Slicing!
print(taquerias)
print(taquerias[0:len(taquerias):2])#esto se le llama Slicing!
print(taquerias[1:3 + 1])#Slicing 
#Matriz 
m= [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

print(np.array(m))



