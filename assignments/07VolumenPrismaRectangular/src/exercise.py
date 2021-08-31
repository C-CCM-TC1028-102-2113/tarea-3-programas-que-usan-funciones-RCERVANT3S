
def main():
  #escribe tu código abajo de esta línea
    pass

def areat(altura, base):
    al = altura
    bas = base
    area = float
    area = al * bas     
    
    return area

  
def vol(areat,profundidad):
 volumen = float
 volumen = globals()['area'] * profundidad
  
 print (volumen)
 return volumen

altura = float(input("Dame la altura: "))
base = float(input("Dame la base: "))
areat(altura, base)

profundidad = float(input("Dame la profundidad: "))
area = areat(altura, base)
vol(area ,profundidad)   



if __name__ == '__main__':
    main()
