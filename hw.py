def valid(x):
    while True:
        try:
            entero=int(x)
            return entero
        except TypeError:
            print("El valor ingresado no es entero")
            break
        except ValueError:
            print("El valor ingresado no es entero")
            break

def largo(x):
    while True:
        if len(x)==4:
            return x
        else:
            print("Ingresar número de factura correcto")
            x = input("ingresar número de facura: ")

def menu():
    sel=[]
    op=[1,2,3]
    #pend=[]
    cobradas=[]
    data = {}
    print("1. Desea añadir una factura? (Opcion 1)")
    print("2. Desea pagar una factura? (Opción 2)")
    print("3. Desea terminar? (Opción 3)")
    print()
    sel=input("Ingresar selección: ")
    x=valid(sel)
    while x not in op:
        print("Ingresar valor correcto: ")
        sel=input("Ingresar selección: ")
        x=valid(sel)
        print()
    else:
        while True:
            if x==1:
                elemnt=input("Número de elementos a ingresar: ")
                elemnt=valid(elemnt)
                for i in range(elemnt):
                    num_fact=input("Ingresar el número de factura: ")
                    num_fact=largo(num_fact)
                    monto=input("Ingresar el costo: ")
                    monto=valid(monto)
                    #pend.append(monto)
                    data[num_fact]=monto
                print(f"El diccionario pendiente es: {data}")
                total=sum(data.values())
                print(f"El total de pendiente es de: {total}")
                print(f"El total de facturas cobradas es:{cobradas}")
                print("----------------------------------------------------")
                x=[]
            elif x==2:
                #data={"1234":321,"4321":123}
                factura = input("Ingrese el número de factura: ")
                factura = largo(factura)
                print(data)
                if factura in data:
                    cobradas.append(data.get(factura))
                    del data[factura]
                total_cob=(sum(cobradas))
                total=sum(data.values())
                print(f"El diccionario de pendiente es: {data}")
                print(f"El total de pendiente es de: {total}")
                print(f"El total de facturas cobradas es:{total_cob}")
                x=[]
            elif x==3:
                print("----------------------------------------------------")
                break
            else:
                sel=input("Ingresar selección: ")
                x=valid(sel)  
                #break

                
        
 
menu()