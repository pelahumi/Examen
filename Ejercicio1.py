import random

i = int(input("Introduce un número del 1 al 5: "))
print("La cadena de texto tendrá una longitud de " + str(i))

def Stuart():
    string = "bcdfghjklmnñpqrstvwxyz"
    print("Stuart tienes que formar todas las combinaciones posibles con las siguientes letras: ")

    numero = 0
    while numero < i:
        string_aleatorio = random.choice(string)
        print(string_aleatorio,end="")
        numero = numero + 1

    score_stuart = 0
    while True:
        respuesta = input("\n" + "Tienes alguna combinación: ")

        if respuesta == "Sí" or respuesta == "Si" or respuesta == "si" or respuesta == "sí":
            combinacion = input("Introduce la combinación: ")
            score_stuart = score_stuart + 1
        else:
            break
        print(score_stuart)








        


    
    
        

Stuart()
