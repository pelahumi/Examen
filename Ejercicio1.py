import random

i = int(input("Introduce un número del 1 al 5: "))
print("La cadena de texto tendrá una longitud de " + str(i))

def Stuart_Kevin():
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
            combinacion = input("Introduce la combinación: ")

            if combinacion not in lista:
                print("Error introduce una combinacion con las letras correspondientes.")

            else:
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
            print("La puntucación de Stuart es: " + str(score_stuart))
            break

    string = "aeiou"
    print("Kevin tienes que formar todas las combinaciones posibles con las siguientes letras: ")

    numero = 0
    while numero < i:
        string_aleatorio = random.choice(string)
        print(string_aleatorio,end="")
        numero = numero + 1
    
    score_kevin = 0

    while True:
        respuesta = input("\n" + "Tienes alguna combinación: ")

        if respuesta == "Sí" or respuesta == "Si" or respuesta == "si" or respuesta == "sí":
            list(string_aleatorio)
            lista = list(string_aleatorio)
            combinacion = input("Introduce la combinación: ")

            if combinacion not in lista:
                print("Error introduce una combinacion con las letras correspondientes.")

            combinaciones = list(combinacion)

            if combinacion in  combinaciones:
                print("La combinación está repetida")

            else:
                #Puntuación
                if len(combinacion) == 1:
                    score_kevin = score_kevin + 1

                if len(combinacion) == 2:
                    score_kevin = score_kevin + 2

                if len(combinacion) == 3:
                    score_kevin = score_kevin + 3
                
                if len(combinacion) == 4:
                    score_kevin = score_kevin + 4
                
                if len(combinacion) == 5:
                    score_kevin = score_kevin + 5
            
        
        else:
            print("La puntucación de Kevin es: " + str(score_kevin))
            break
            
        if score_stuart > score_kevin:
            print("El ganador es Stuart")
        if score_kevin >score_stuart:
            print("El ganador es Kevin")
        else:
            print("Empate, no hay ganador")

Stuart_Kevin()


        


    
    
        



