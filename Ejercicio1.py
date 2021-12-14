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
            list(string_aleatorio)
            lista = list(string_aleatorio)
            print(lista)
            combinacion = input("Introduce la combinación: ")

            if combinacion not in lista:
                print("Error introduce una combinacion con las letras correspondientes.")

            combinaciones = list(combinacion)

            if combinacion in  combinaciones:
                print("La combinación está repetida")

            #Puntuación
            if len(combinacion) == 1:
                score_stuart = score_stuart + 1

            if len(combinacion) == 2:
                score_stuart = score_stuart + 2

            if len(combinacion) == 3:
                score_stuart = score_stuart + 3
            
            if len(combinacion) == 4:
                score_stuart = score_stuart + 4
            
            if len(combinacion) == 5:
                score_stuart = score_stuart + 5
   
        else:
            print("La puntucación de Stuart es: " + score_stuart)
            break








        


    
    
        

Stuart()
