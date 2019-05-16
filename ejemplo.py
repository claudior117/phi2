# -*- coding: utf-8 -*-
import time
import phi2 as phi2 #Importa libreria phi2(la carpeta phi2 debe
                               #estar dentro de la carpeta del proyecto
phi2.set("com9", 9600)  #define el puerto de comunicacion
phi2.open()  #abre la conexion con phi2
time.sleep(1) #espera 1 seg para asegurarse que la conexion esta establecida
i=0
while True: #bucle infinito
    i += 1
    print("Encendido " + str(i) + " veces")
    phi2.write(255)  #envia un valor alto(5V) a todos los pines de salida(0-7)
    time.sleep(5) #mantinene encendido 3 segundos
    phi2.down() #setea todas las salidas a nivel bajo (0-7)
    time.sleep(1) #mantiene apagado 1 segundo

#Programa que permite encender todos los puertos standars(0-7)
#por 3 segundos y luego apagarlos por 1 segundo


