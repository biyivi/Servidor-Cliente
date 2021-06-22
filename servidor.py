'''
coded by:  
                             
    )                        
 ( /( (   (    (    )   (    
 )\()))\  )\ ) )\  /((  )\   
((_)\((_)(()/(((_)(_))\((_)  
| |(_)(_) )(_))(_)_)((_)(_)  
| '_ \| || || || |\ V / | |  
|_.__/|_| \_, ||_| \_/  |_|  
          |__/            
'''
#importamos socket
import socket 

#creando un socket para el servidor
s = socket.socket()

#mensaje que nos indica que se creo correctamente
print('''
                         ____
                  /^\   / -- )
                 / | \ (____/
                / | | \ / /
               /_|_|_|_/ /
                |     / /
 __    __    __ |    / /__    __    __
[  ]__[  ]__[  ].   / /[  ]__[  ]__[  ]
|__            ____/ /___           __|
   |          / .------  )         |
   |         / /        /          |
   |        / /        /           |
~~~~~~~~~~~~-----------~~~~~~~~~~~~~~~~~
''')
print("Socket creado !!")

'''
    *******************************************************************

    indicamos la ip y el puerto, puede ser el localhost o tu ip privada
    en este caso usare el "localhost" y el puerto "8081"

    *******************************************************************
'''
s.bind(('localhost', 8081)) #aqui debes cambiar localhost por tu ip

s.listen(3)

#mensaje que indica que esta esperando conexiones
print("Esperando conexiones./././")

while True:
    c, addr = s.accept()
#recibiendo el mensaje del nombre del cliente y transformadolo de formato "bytes"
#a "string" con " .decode()"
    name = c.recv(1024).decode()
    print("Conectado con: ", addr, name)

#enviando mensaje en formato "byte" a los clientes
    c.send(bytes('Bienvenido a mi servidor!!', 'utf-8'))



