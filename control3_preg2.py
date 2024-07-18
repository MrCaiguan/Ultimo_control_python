
def convierte_negativo(lista):
    cont=0
    for x in lista:
        lista[cont]=x*-1
        cont+=1
lista=[]

for x in range(10):
     num=int(input("Ingrese un numero positivo:"))
     lista.append(num)
  
    
convierte_negativo(lista)
print(lista)