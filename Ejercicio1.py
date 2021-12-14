import random

i = int(input("Introduce un número del 1 al 5: "))
print("La cadena de texto tendrá una longitud de " + str(i))

def Stuart():
    string = "bcdfghjklmnñpqrstvwxyz"
    print("Stuart tienes que formar todas las combinaciones posibles con las siguientes letras: ")

    numero = 0
    while numero < i:
        string_aleatorio = random.choice(string)
        print(string_aleatorio,end=" ")
        numero = numero + 1
        


    
    
        

Stuart()
