# -*- coding: utf-8 -*-
"""Introduccion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eX5J3kSvlJoVfRCkHpyzkREdlU4POWKR
"""





"""# Introduccion a objetos.

Objetos que veremos son:

1.   Numeros(int, float), strings("hola").
2.   Listas.
3.   Variables.



Referencia: [Youtube](https://www.youtube.com)

Hay funciones que estan cradas dentro de Python.
"""

5+2 #Suma

5*7 #Multiplicacion

2**3 #Potencia

2/3 #Division

3%2 #Residuo

"""Una ecuacion:
$$ax^2+bx+c=0$$

LaTex
$$e^{i\pi}+1=0.$$
"""

5//2 #Division al piso

print("Hola, mundo")

nombre = "Isaac"
print(nombre)

x = "5"
print(x)

"""Funcion type dice
¿Que tipo de ojbeto esta escrito?
"""

x=5
y=2

type(x/y)

type(x)

type(nombre)

print(type(x/y))
print(type(x))
print(type(nombre))

"""## Listas

Las listas con objetos que se escriben con []
"""

L = []
type(L) # Nos dice que tipo de objeto es

# La funcion range() (es un generador de etiquetas)
range(10)

for i in range(10):
  print(i)

for i in range(10):
    L.append(i) # Agrega elementos a la lista
print(L)

L[0:4]

L[1:]

P = []
for i in range(10):
    if i % 2 == 0:
        P.append(i)
P

I = [i for i in L if i%2==1]

I

P + I #Junta las listas

I + P

"""Conjuntos"""

sP =set(P)
sI =set(I)

print(sP)
print(sI)

sP.intersection(sI)