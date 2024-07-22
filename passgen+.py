import string 
import random

generador = int(input("Elige de que manera quieres crear la contraseña: \n 1- Letras, numeros y signos \n 2-Letras y numeros \n 3-Solo Letras \n 4-Solo Numeros \n 5-Salir \n"  ))

while generador != 0:

    if generador == 1:

        longitud = int(input("Cuantos caracteres deseas que tenga la contraseña: "))

        caracteres = string.ascii_letters + string.digits + string.punctuation

        contrasena = "".join(random.choice(caracteres) for i in range(longitud))

        print("La contraseña generada es: " + contrasena)

    elif generador == 2:

        longitud = int(input("Cuantos caracteres deseas que tenga la contraseña: "))

        caracteres = string.ascii_letters + string.digits 

        contrasena = "".join(random.choice(caracteres) for i in range(longitud))

        print("La contraseña generada es: " + contrasena)

    elif generador == 3:

        longitud = int(input("Cuantos caracteres deseas que tenga la contraseña: "))

        caracteres = string.ascii_letters 

        contrasena = "".join(random.choice(caracteres) for i in range(longitud))

        print("La contraseña generada es: " + contrasena)

    elif generador == 4:

        longitud = int(input("Cuantos caracteres deseas que tenga la contraseña: "))

        caracteres = string.digits 

        contrasena = "".join(random.choice(caracteres) for i in range(longitud))

        print("La contraseña generada es: " + contrasena)

    elif generador == 5:

        print("Adios!")
        break 
