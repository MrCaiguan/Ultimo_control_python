
def potencia(num,exp):
 if exp==0:
    return 1
 else:
    resultado=num*potencia(num,exp-1)
    return resultado
print(potencia(2,7))