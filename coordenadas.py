"""Programa para definir
la ubicación de una coordenada"""

from re import X


print("\n♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("♦♦♦♦♦♦♦ Coordenadas ♦♦♦♦♦♦♦")
print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠" + "\n")


# input

x = int(input("Cordeanda del eje x: "))
y = int(input("Cordenada del eje y: "))

# processing


if x > 0 and y > 0:
    msj = ("se encuentra en el primer cuadrante")
elif x < 0 and y < 0:
    msj = ("se encuentra en el tercer cuadrante")
elif x < 0 and y > 0:
    msj = ("se encuentre en el segundo cuadrante")
elif x > 0 and y < 0:
    msj = ("se encuentra en el cuarto cuadrante")
elif x == 0 and y != 0:
    msj = ("se encuentra en el eje y")
elif x != 0 and y == 0:
    msj = ("se encuentra en el eje x")
else: 
    msj = ("esta en el origen")

# output

print("\nLa coordenada " + msj + "\n")