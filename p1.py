#importando biblioteca
import matplotlib.pyplot as plt



#Funciones en python

# Prestamo en NU

prestamo = 2000
tasa_interes_mensual = .29
#Meses 
tiempo = range(13)
trabajo = 11000

def interes_compuesto(capital_inicial, interes, tiempo):
    ic = capital_inicial * (1 + interes) ** tiempo
    return ic

historial_prestamo = []
for t in tiempo:
    historial_prestamo.append(interes_compuesto(prestamo, tasa_interes_mensual, t))

plt.plot(tiempo, historial_prestamo)
plt.show()