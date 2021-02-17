#from IPython.display import Image
from skimage import io
#Condicionales (pt. II)
"""Los condicionales los utilizaremos para validar si se cumple una o más condiciones para ejecutar cierto bloque de código,
    incluso para validar si algúin dato forma parte de una colección.
Ejemplo:
>>> 1 in [1, 2, 3, 4, 5]"""
taquerias = [
    "Los Güeros",       # 0 La pocision en que se encuantra el elemento en la lista 
    "Veloz",            # 1
    "Tacos Los Papis",  # 2
    "Takesabroso",      # 3
    "Takos El Rodo"     # 4
]
print(taquerias)#taquerias en leon 
"Taqueria El inge " in taquerias #la palabra in es una reservada para saber si hay un objeto en una lista o en una dupla 
taqueria = "Taqueria El inge"
if taqueria in taquerias:
    print("Esta en Leon ")
else:
    print("no se donde estas")
print(taquerias[3])
print(len(taquerias))
print(taquerias[1])

#Ciclos – for
"""
Python tiene un ciclo basado en colecciones o en iteradores. Este tipo de ciclo itera sobre una colección de objetos,
en lugar de especificar valores o condiciones numéricos, este ciclo se llama ciclo for.
"""
#Sintaxis 
""" 
#Ejemplo en lenjuague C 
for (int i=0; i < 100; i++) {
    // Ciclo
}
EN PYTHON es soobre colecciones 
For element in collection:
    #Block of code that iterates over the collection
"""
print(taquerias)
for takeria in taquerias:
    n_nombre= takeria.upper()#la funcion upper es para que la cadena de texto se ponga en mayusculas 
                            # mas funciones como lower(), que lo pone en minusculas 
                            # o la otra que es capitalize() es para que la prime letra sea mayuscula 
    print(n_nombre)
#En el ciclo anterior para cada taqueria dentro de taquerias , me regresara el nombre de cada una 
#de las taquerias ahi descritas 
#Para que el ciclo for funcione de alguna manera como en c en python nos auxiliamos de una funcion 
# llamada Range 
range(1,100,2)#done rage (n= donde inicia, n2= hasta donde llega, n3= como llega ahi )
#Si yo quisiera ver los valores de ese rango lo hacemos una lista 
m= list(range(1,11))
print(m)
#Ejemplo de coomo integrar el range en el ciclo for 
for i in range(len(taquerias)):
    print(taquerias[i])
#Pase de lista
alumnos = [
    "Alexis",
    "Anneliesse",
    "Anonymous",
    "Rodo"
]
for alumno in alumnos:
    print(alumno)
alumnos.append("Richard")#la funcion append añade un elemento al final de una lista 

for i in range(5):
    print((i + 1) * "*")


perritoz = [
    "https://i.pinimg.com/originals/70/fa/97/70fa97bac09e524bae4c006a1ead5512.jpg",
    "https://i.pinimg.com/originals/21/c1/13/21c113e05f1a219989a0b07a03b1577a.jpg",
    "https://i.pinimg.com/originals/63/96/0c/63960c5db954115a0b5d8868c0c7e8a0.jpg"
]
print(perritoz)
image=io.imread(perritoz[1])
print(image.shape[1])

