def main():
  #escribe tu código abajo de esta línea
  pass

def es_bisiesto(bisiesto):
    if bisiesto % 4 == 0 :
        if bisiesto % 100 != 0:
            print("False")

        elif bisiesto % 100 == 0 and bisiesto % 400 == 0: 
             print("True")
    else:   print("False")

bisiesto = int(input())
es_bisiesto(bisiesto)

if __name__ == '__main__':
    main()
