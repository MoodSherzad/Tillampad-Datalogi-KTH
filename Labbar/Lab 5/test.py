def utskrift(lista):
    if len(lista) > 0:

        utskrift(lista[1:]) # När vi byter plats på printen och utskrift så skrivs listan omvänd
        
        print(lista[0])

        

lista = [1, 2, 3, 4, 5]
utskrift(lista)  
