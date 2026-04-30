print("""
       Bienvenido al sistema de circuferencia
    
  ██████   ██████   ██           ♥♥  ♥♥
 ██       ██    ██  ██          ♥   ♥  ♥    <3
  █████   ██    ██  ██          ♥      ♥
      ██  ██    ██  ██           ♥    ♥
 ██████    ██████   ██████        ♥  ♥ 
                                    ♥
                                                                               
                    
""")

while True:
    area = 0
    peri = 0
    print("Area y perímetro de la circuferencia")
    print("====================================")
    print()
    radio = float(input("Ingrese radio: "))
    area = 3.14 * radio * radio
    peri = 2 * 3.14 * radio
    print("Mostrar resultado")
    print("Area:       ", round(area, 2))
    print("perimetro : ", round(peri, 2))
    while True:
        try:
            op = int(input("Desea continuar? SI=1/NO=0: "))
            if op == 0 or op == 1:
                break
            else:
                print("Opción no válida, intente de nuevo")
        except:
            print("Entrada no válida, intente de nuevo")
    if op == 0:
        break
print()
print("Gracias por usar el programa, hasta luego!")
print("♥♥♥♥")