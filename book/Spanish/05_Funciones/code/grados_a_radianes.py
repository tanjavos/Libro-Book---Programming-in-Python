import math
grados = float(input("¿Cuantos grados quieres convertir a radianes? "))
radianes = grados / 360.0 * 2 * math.pi
print("{0} grados es {1} radianes".format(grados, math.sin(radianes)))
