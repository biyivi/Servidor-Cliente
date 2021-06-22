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

#creando un socket para el cliente
c = socket.socket()

#conectando con el servidor en este caso es el "localhost" y el mismo puerto
#"8081"
c.connect(('localhost', 8081))

#preguntando al cliente para que elija su nombre de usuario "input(pregunta)"
print('''
    <=======]}======
      --.   /|
     _\"/_.'/
   .'._._,.'
   :/ \{}/
  (L  /--',----._
      |          \\
     : /-\ .'-'\ / |
biyivi\\, ||    \|
       \/ ||    ||
''')

name = input("Ingrese su nombre de usuario: ")
#enviando mensaje en formato "byte"
#utf-8= formato de codificacion de caracteres
c.send(bytes(name, 'utf-8'))

#convirtiendo el mensaje recibido de formato "byte" a "string" con: " .decode()"
print(c.recv(1024).decode())
