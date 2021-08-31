def main():
  #escribe tu código abajo de esta línea
    pass
def pliegos(papelb, plum):
    papelb = 12 * papelb
    plum = 35 * plum
    if papelb < plum:
        print("El número máximo de tarjetas que se pueden hacer es:",papelb)
    elif papelb > plum:
        print("El número máximo de tarjetas que se pueden hacer es:",plum)

        
papelb = int(input("Dame la cantidad de pliegos de papel albanene: "))
plum = int(input("Dame la cantidad de plumones: "))
pliegos(papelb, plum)




if __name__ == '__main__':
    main()
