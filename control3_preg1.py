
def solo_numeros(s):
    try:
        float(s)
        return True
    except :
        return False
s =input("Ingrese una palabra : ")
print(solo_numeros(s))   
 
