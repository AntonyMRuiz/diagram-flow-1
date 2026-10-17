# variables
capital = 1000000
ganancias = 0
gastos = 0
servicio = 300000
comida = 700000
ropa = 200000
varios = 300000
arriendo = 500000
cine = 100000
estreno = 400000

# overview - introduccion
print("Use el capital, para generar ganacias")

ganacias = 3000000

# mostrar en consola los procesos
print("Tus ganancias este mes fueron : $",ganacias)

#ejecutar el proceso
ganacias = ganacias - servicio
print("He pagado los servicios y fue de : $" + str(servicio) + " y aun quedan : $"+ str(ganacias))

ganacias = ganacias - ropa
print("He pagado la ropa y fue de : $" + str(ropa) + " y aun quedan : $"+ str(ganacias))

ganacias = ganacias - arriendo
print("He pagado el arriendo y fue de : $" + str(arriendo) + " y aun quedan : $"+ str(ganacias))

ganacias = ganacias - comida
print("He pagado la comida y fue de : $" + str(comida) + " y aun quedan : $"+ str(ganacias))

ganacias = ganacias - varios
print("He pagado los varios y fue de : $" + str(varios) + " y aun quedan : $"+ str(ganacias))

if(ganacias>0):
    # flujo de verdad
    ganacias = ganacias - cine
    print("te viste toy story 5")
else:
    # flujo de falsedad
    print("Tome agua y vea tv, no hay plata")

if(ganacias>=estreno):
    # flujo de verdad
    ganacias = ganacias - estreno
    print("la pinta para el 31")
else:
    # flujo de falsedad
    print("Toco repetir pinta")

print("Nos sobro al final del mes: $"+str(ganacias))


"""
    - Ejemplo para entender, decisiones con multiples componentes (condiciones)
 """

tengo_lavadora = "no"
tengo_1_tapita_de_suavizante = "si"
tengo_agua = "si"


if(tengo_lavadora == "si" and tengo_1_tapita_de_suavizante == "si" and tengo_agua == "si"):
    print("Puedo lavar")
else:
    print("Pailas, ponerse la ropa al reves")


lavadora = True
suavizante = False
agua = True

if(lavadora and suavizante and agua):
    print("Puedo lavar")
else:
    print("Pailas, ponerse la ropa al reves")