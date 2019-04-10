from linkedQFile import *
import sys
import string
from molgrafik import *
#from hashtest import *
q = LinkedQ()
parantes = LinkedQ()
atomLista = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr',
  'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 
  'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 
  'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 
  'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
   'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 
   'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm',
    'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 
	'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

class Syntaxfel(Exception):
	pass

def storeMolekyl(molekyl):
	for symbol in molekyl:
		q.enqueue(symbol)
	return q

def readmol():
    mol_objekt = readgroup()

    if q.isEmpty():
        return mol_objekt
    elif q.peek() is ")":
        if parantes.isEmpty():
            raise Syntaxfel("Felaktig gruppstart vid radslutet ") 
        return mol_objekt
    else:
        mol_objekt.next = readmol()
    return mol_objekt

def readgroup():
    rut_objekt = Ruta()
    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    if q.peek().isdigit():
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")

    if q.peek().isalpha():
        rut_objekt.atom = readAtom()
        if q.peek() is None:
            return rut_objekt
        if q.peek().isdigit():
            antal = int(number())
            rut_objekt.num = antal
            

    elif q.peek() is "(": #PATANTESER
        parantes.enqueue(q.dequeue())
        if q.peek().isdigit():
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        rut_objekt.down = readmol()
        if not q.peek() is ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet ")

        if q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet ")
        else:
            parantes.dequeue()
            q.dequeue() #PARANTESER
            if q.isEmpty():
                raise Syntaxfel("Saknad siffra vid radslutet ")
            antal = int(number())
            rut_objekt.num = antal			
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
    return rut_objekt

def readAtom():
	if q.peek().isupper():
		atom = q.dequeue()
		#print(r, "readAtom stor bokstav")
	else:
		raise Syntaxfel("Saknad stor bokstav vid radslutet ")
	if not q.peek() is None:
		if q.peek().islower():
			atom = atom + q.dequeue()
	if atom in atomLista:
		return atom
	else:
		raise Syntaxfel("Okänd atom vid radslutet ")

def number(): #FIXAD DELUX
    n = ""
    lista = []
    if q.peek().isdigit():
        if q.peek() == "0":
            lista.append(q.dequeue())
            raise Syntaxfel("För litet tal vid radslutet ")
        elif q.peek() == "1":
            try:
                if q.peekNext().isdigit():
                    while q.peek().isdigit():
                        lista.append(q.dequeue())

                        break
                else:
                    #q.dequeue()
                    raise Syntaxfel("För litet tal vid radslutet ")
            except:
                lista.append(q.dequeue())
                raise Syntaxfel("För litet tal vid radslutet ")
            
        while q.peek() != None:
        
            if q.peek().isdigit():
                lista.append(q.dequeue())

            else:
                break
        for i in range(len(lista)):
            n = n + lista[i]

        return n
    else:
        raise Syntaxfel("Saknad siffra vid radslutet ")

def firstError(): #FIXAD DELUX
	notDequeue = ""
	while not q.isEmpty():
		notDequeue = notDequeue + q.dequeue()
	return notDequeue

def readFormel(molekyl): #FIXAD halvt
    molekyl = molekyl.strip()
    storeMolekyl(molekyl)
    try:
        mol_objekt = readmol()
        if parantes.isEmpty is False:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        print("Formeln är syntaktiskt korrekt")
        return mol_objekt
    except Syntaxfel as error:
        return str(error) + firstError()



def main():
    in_data = "Si(C3(COOH)2)4(H2O)7" # väntar input
    mg = Molgrafik()
    if in_data != "q":  # hashtag är en stoppkolss
        p = readFormel(in_data)
        firstError()
        print(p.atom) #Si
        print(p.next.atom)#()
        print(p.next.num)#4
        print(p.next.down.atom)#C
        print(p.next.down.num)#3
        print(p.next.down.next.atom)#()
        print(p.next.down.next.num)#2
        print(p.next.down.next.down.atom) #C
        print(p.next.down.next.down.next.atom) #O
        print(p.next.down.next.down.next.next.atom)#O
        print(p.next.down.next.down.next.next.next.atom)#H
        print(p.next.next.atom)#()
        print(p.next.next.num)#7
        print(p.next.next.down.atom)#H
        print(p.next.next.down.num)#2
        print(p.next.next.down.next.atom)#O
        mg.show(p)
        q.Empty() #måste rensa känkade listan
        parantes.Empty() #måste rensa känkade listan
        


if __name__ == '__main__':
	main()

