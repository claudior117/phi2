Libreria PHI Version 4.1 Final (incluye modulo Python y Sketch Arduino) para arduino Uno/Nano

*****************************************************************
Autor: Claudio Ravagnan - Escuela Tecnica Rojas(Buenos Aires-Argentina)
*****************************************************************

Phi2(Python Hardware Interfaz) es una libreria en python y un sketch para arduino que permite manipular entradas y salidas de un
arduino a travez del puerto serie de la pc y desde el lenguaje python a modo de GPIO. DiseÒado solo a nivel educativo para permitir tener
entradas y salidas por hardware desde lenguaje python lo que equivale a emular un raspberry en cualquier pc.



Requerimientos e instalacion:

1) Instalar Python3 o superior (asegurarse tener direccionado a python 3 en la variable path)
2) Instalar el modulo pyserial, para ello primero hay que actualizar el pip:
	python -m pip install --upgrade pip
        pip install pyserial

   	Si no tenemos internet  python -m pip install  ruta\pyserial-3.4-py2.py3-none-any.whl
	(El archivo se encuentra en la carpeta instaladores)

3)Conectar el phi2 y verificar 
3) copiar la carpeta phi2 dentro de la carpeta lib de python
4) En la primera linea del programa colocar:
	from phi2 import *
	phi2.set("com8", 9600)  


Configuracion:

Antes de empezar a trabajar debemos ir a el administrador de dispositivos y verificar que nuestra pc reconocio al dispositivo
phi2 y le asigno un puerto de comunicacion (com) seguido de un numero como 3, com4, com5, etc. Dicha denominacion es importante 
para cpoder indicarle a nuestro programa paython porque canal va trasnmitir de y desde la poc al phi2. Esto lo hacemos como
vimos en el punto de requerimientos con el comando:

phi2.set("com8", 9600) 

En caso que la pc muestre dispositivo no reconocido (usb) debemos instalar el driver adjunto dentro de la carpeta phi2




*************************************
Esquema de Entradas y Salidas
*************************************

Salidas (0-7) --> Corresponden del 2 al 9 de arduino 

Entradas (0-7) --> Corresponden del A0 al A7 de arduino (como entradas digitales arduino numeradas del 14 al 19) 

Salidas PWM(1,3,4,7,8) --> Correspondientes a la 3,5,6,9,10 de arduino

E/S uso generales (10-13)

Sensor ultrasonido --> Tigger 12 - Echo 11  del arduino 

Motor Servo  -->  Pin 10


*************************************
Caracteristicas Electricas
*************************************

Las salidas digitales trabajan con 5v 40 mA y se inicializan a valor LOW

Las entradas estan configuadas en PULLUP esto quiere decir que siempre leer· 1 o high cuando un pulsador conectado a la entrada
este abierto y LOW o 0 cuando este pulsado. Siempre se debe conectar el pulsador a masa


input 2 ----------- pulador ------------gnd


Nunca se debe tener ni en las entras ni e las salidas valores de tension negativos o superiores a 5 V





*******************************
Funciones:
*******************************

open(): Abre una conexion serie entre python y el Phi2

close(): cierra la conexion serie entre python y phi2

set(puerto, velocidad)  --> Define la velocidad y el numero de puerto a utilizar desde python phi
			    
write(dato) --> Permite escribir sobre los puertos de salida numerados del 0 al 7 y corresponden 
                fisicamente a los puertos 2 a 9 del arduino (0-2; 1-3; ...). El dato que se debe
		enviar es un numero decimal entre 0 y 255. Este numero es la correspondencia
                con los valores binarios de los puertos, por ejemplo si mando el numero 4, en binario 
		es 00000100, lo que indica que se pondra en 1(high) la salida 2 y las demas se fijaran 
		en 0.



Down() --> setea todas las salidas a LOW, equivale a write(0)

Up() --> setea todas las salidas en high, equivale a write(255)

read(p) --> lee los puertos de entrada enumerados del 0-7 (arduino 14-19 o A0 al A7) y devuelve:
		p=9 --> El estado de todos los puertos en una cadena binaria de tipo 00000000 al 11111111
                        segun el estado de los puertos del 0-7
		p= (0-7) El estado(0-1) del puerto solicitado
		
		La devolucion es simpre un valor de tipo String


------------------------------------------------------------
version 3.1
------------------------------------------------------------
pwm(puerto, intensidad): Realiza una modulacion de pulsos en los puertos 1,3,4,7,y 8 coprrespondients
			a los puertos 3,5,6,9 y 10 de arduino, La intesidad es una valor de 0 a 9 que
			ser· multiplicado por 25 para determinar el porcentaje de modulacion


 
-------------------------------------------------------------
Version 4.0  --> ultrasonido
-------------------------------------------------------------
us_read()  --> recibe un dato numerico(string) en centimetros, es necesario conectar el sensor ultrasonido en los pines 12 tigger y 11 echo. Se recomienda poner un delay de al menos 0.5 entre lectura y lectura

-------------------------------------------------------------
Version 4.1  --> servomotor
-------------------------------------------------------------
sm_write(angulo) --> envia el angulo a mover el servomotor --> Pin 10 servomotor


*****************************
Veriosnes
*****************************
1.0 Incluye Write, set
1.1 Opoen, close, down, up
2.1 Write_l, Writeh, Read
3.1 Pwm, incorpota 8 outputs, 4 outpus extendidas, 8 inputs
4.0 Sensor Ultrasonido   --> Se sacan las salidas extendidas del 10 al 13 porque se usaran para los sensores. 
4.1 Servomotor  --> pin 10




********************************
Ejemplos
********************************

1)Simple
#Programa que permite encender todos los puertos standars(0-7)
#por 3 segundos y luego apagarlos por 1 segundo
# -*- coding: utf-8 -*-
import time, phi2.phi2 as phi2 #Importa libreria phi2(la carpeta phi2 debe
                               #estar dentro de la carpeta del proyecto
phi2.set("com8", 9600)  #define el puerto de comunicacion
phi2.open()  #abre la conexion con phi2
time.sleep(1) #espera 1 seg para asegurarse que la conexion esta establecida
i=0
while True: #bucle infinito
    i += 1
    print("Encendido " + str(i) + " veces")
    phi2.write(255)  #255 binario es 11111111 pone todas las salida(0-7) en Alto
    time.sleep(3) #mantinene encendido 3 segundos
    phi2.down() #setea todas las salidas a nivel bajo (0-7). Es igual a write(0)
    time.sleep(1) #mantiene apagado 1 segundo



2)Sistema de control de semaforos con interfaz grafica

#uso phi2 para controlar el encendido de los leds que
#representan a los semaforo(uso 6 salidas)

#semaforo1 conexionado:
    #rojo: salida0 phi2 ----> pin2 arduino
    #amarillo: salida1 phi2 ----> pin3 arduino
    #verde: salida2 phi2 ----> pin4 arduino

#semaforo2 conexionado:
    #rojo: salida4 phi2 ----> pin6 arduino
    #amarillo: salida5 phi2 ----> pin7 arduino
    #verde: salida6 phi2 ----> pin8 arduino



from tkinter import *
from time import  *
import phi2



def rojo():
    canvas.create_oval(100, 10, 180, 80, width=2, fill='red', outline='')
    canvas.create_oval(100, 90, 180, 160, width=2, fill='gray', outline='')
    canvas.create_oval(100, 170, 180, 240, width=2, fill='gray', outline='')


def amarillo():
    canvas.create_oval(100, 10, 180, 80, width=2, fill='gray', outline='')
    canvas.create_oval(100, 90, 180, 160, width=2, fill='yellow', outline='')
    canvas.create_oval(100, 170, 180, 240, width=2, fill='gray', outline='')


def verde():
    canvas.create_oval(100, 10, 180, 80, width=2, fill='gray', outline='')
    canvas.create_oval(100, 90, 180, 160, width=2, fill='gray', outline='')
    canvas.create_oval(100, 170, 180, 240, width=2, fill='green', outline='')


def rojo2():
    canvas2.create_oval(100, 10, 180, 80, width=2, fill='red', outline='')
    canvas2.create_oval(100, 90, 180, 160, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 170, 180, 240, width=2, fill='gray', outline='')


def amarillo2():
    canvas2.create_oval(100, 10, 180, 80, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 90, 180, 160, width=2, fill='yellow', outline='')
    canvas2.create_oval(100, 170, 180, 240, width=2, fill='gray', outline='')


def verde2():
    canvas2.create_oval(100, 10, 180, 80, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 90, 180, 160, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 170, 180, 240, width=2, fill='green', outline='')





def apagar():
    canvas.create_oval(100, 10, 180, 80, width=2, fill='gray', outline='')
    canvas.create_oval(100, 90, 180, 160, width=2, fill='gray', outline='')
    canvas.create_oval(100, 170, 180, 240, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 10, 180, 80, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 90, 180, 160, width=2, fill='gray', outline='')
    canvas2.create_oval(100, 170, 180, 240, width=2, fill='gray', outline='')


vent1 = Tk()
vent1.title("Mi primer ventana")
vent1.geometry("600x600")
etiq1 = Label(vent1, text="Sistema de Sem√°foros")
etiq1.pack()
canvas = Canvas(width=200, height=300, bg='blue')
canvas.pack(side = LEFT)
canvas.create_text(50,10,text="Sem√°foro 1")

canvas.update()

canvas2 = Canvas(width=200, height=300, bg='blue')
canvas2.pack(side = RIGHT)
canvas2.create_text(50,10,text="Sem√°foro 2")


#checkbox
cboxvar = IntVar()  #creo una variable entera(puede ser BooleanVar) para almacenar el estado del control
cbox = Checkbutton(vent1, text="Intermitente", variable = cboxvar)  #creo el control
cbox.place(x=20, y=70) #coloco el checkbox en la ventana(lo puedo poner en el canvas tamb ien)

#scale
scalevar = IntVar()
scale = Scale(vent1, variable = scalevar, from_=1, to=10, label = "Velocidad en segundos", orient = HORIZONTAL )
scale.pack()

label = Label(vent1)
label.pack()



#variable de retardo
t = 4

apagar()
canvas.update()
canvas2.update()
sleep(t)
LOOP_ACTIVE = True
led = "R"
phi2.set("com9", 9600)
phi2.open()
sleep(1)

while LOOP_ACTIVE:
    t = scalevar.get()
    if cboxvar.get()==0:   #con get obtengo el estado del check
        if led == "V":
            verde()
            rojo2()
            vent1.update()
            phi2.write(20) # 20 binario es 00010100 enciende puerto 2 y 4
            sleep(t)       #verde semaforo 1 y rojo semaforo 2
            amarillo()
            rojo2()
            phi2.write(18)
            vent1.update()
            sleep(t)
            led = "R"
        else:
            rojo()
            verde2()
            phi2.write(65)
            vent1.update()
            sleep(t)
            amarillo2()
            rojo()
            phi2.write(33)
            vent1.update()
            sleep(t)
            led = "V"
    else:
        #intermitente
        amarillo()
        amarillo2()
        phi2.write(34)
        vent1.update()
        sleep(t)
        apagar()
        phi2.down()
        vent1.update()
        sleep(t)



3)lector de distnacia con ultrasonido  

##sensor ultrasonido
from time import *
from os import *

import phi2.phi2 as phi2

phi2.set("com8", 9600)
phi2.open()
sleep(1)
system('cls')
while True:
    d = phi2.us_read()
    print("Distancia: " + d)
    sleep(4)



4)Servo Motor
##servo motor
from time import *
from os import *

import phi2.phi2 as phi2

phi2.set("com8", 9600)
phi2.open()
sleep(1)
system('cls')
while True:
    phi2.sm_write(90)
    sleep(3)
    phi2.sm_write(0)
    sleep(3)
    phi2.sm_write(180)
    sleep(3)