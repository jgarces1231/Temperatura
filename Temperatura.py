# Ejercicio No° 2 Programa para convertir unacantidad de grados C en la equivalencia a K y F 

# input 
C = input("Digite la cantidad de grados C a convertir a  ")
C = int(C)

# prosessing 
F = (C*9/5)+32 
K = C+273.15

# output
print("Grados fahrenheit " + str(F))
print("Grados kelvin " +  str(K))