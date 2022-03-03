#Laboratorio 2 de python
#Modelación y simulación 2022
#Chahim Vicenta Imelda Teny Puac

#Librerias
import math
A = 2 #velocidad del llegada
u = 3 #clientes / hora 

print("LABORATORIO M/M/1")
print ()

#Numero promedio de pacientes en el sistema
Ls = A/(u-A)
print ("El promedio de pacientes en el sistema es de ", Ls, "Pacientes")

#Tiempo total que consume un paciente en el consultorio
ws = (1/(u-A))
print("El tiempo que pasa un paciente en el consultorio es de ", ws, "hora")

#Factor de uso del sistema
P = A/u
P1 = P*100
print("Porcentaje de uso del sistema ", P1, "%")

#Numero promedio de pacientes haciendo fila
nosale = pow(A,2) /u*(u-A)
print ("Promedio de pacientes haciendo cola ", nosale, "Pacientes")

#Probabilidad de que el consultorio este vacio
Po = (1-P) *100
print("Probabilidad de que el consultario se encuentre vacio ", Po, "%")

# Probabilidad de que se encuentren 2 pacientes en el mismo sistema
P2 = (1-P) * pow(P, 2) * 100
print("Probabilidad de que se encuentren 2 pacientes en el sistema ", P2, "%")