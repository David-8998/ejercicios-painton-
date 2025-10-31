print(" programa de adivinacion del numero secreto ")
print("tienes 3 intentos para adivinar el numero secreto")
print(" el numero secreto esta entre el 1 al 10") 
entrada=input(" escribe un numero")
numero1=int( entrada) 
if numero1==7:
print(" felicidades adivinate el numero secreto")
else:
print("numero incorrecto, te qquedan 2 intentos") 
entrada=input(" escriba un numeto")
numero2= int( entrada)
if numero2==7:
    print("felicidades adivinaste el numero secreto")
else:
    print("numero incorrecto, te quedan 1 intento")
    entrada=input("escribe un numero") 
    if numero3==7:
        print("felicidades adivinaste el numero secreto")
    else:
        print("lo siento has agotado tus intentos, el numero secreto era 7")
        print("fin del programa")  
     