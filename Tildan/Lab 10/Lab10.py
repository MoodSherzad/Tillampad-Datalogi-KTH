from linkedQFile import *
import string
import sys
from molgrafik import *
q = LinkedQ()
p = LinkedQ()
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

atomer = []
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
        if p.isEmpty():
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
        p.enqueue(q.dequeue())
        if q.peek().isdigit():
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        rut_objekt.down = readmol()
        if not q.peek() is ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet ")

        if q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet ")
        else:
            p.dequeue()
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
		atomer.append(atom)
		return
	else:
		raise Syntaxfel("Okänd atom vid radslutet ")

def number(): #FIXAD DELUX
    if q.peek().isdigit():
        if q.peek() == "0":
            q.dequeue()
            raise Syntaxfel("För litet tal vid radslutet ")
        elif q.peek() == "1":
            try:
                if q.peekNext().isdigit():
                    while q.peek().isdigit():
						# ÄNDRING
                        atomer.append(q.dequeue())
                        break
                else:
                    #q.dequeue()
                    raise Syntaxfel("För litet tal vid radslutet ")
            except:
                q.dequeue()
                raise Syntaxfel("För litet tal vid radslutet ")
            
        while q.peek() != None:
            if q.peek().isdigit():
                q.dequeue()
            else:
                return
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
        if p.isEmpty is False:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        print("Formeln är syntaktiskt korrekt")
        return mol_objekt
    except Syntaxfel as error:
        return str(error) + firstError()



def main():
    in_data = input("Ange molekylen: ") # väntar input
    mg = Molgrafik
    if in_data != "q":  # hashtag är en stoppkolss
        mol_objekt = readFormel(in_data)

        firstError()
        mg.show(mol_objekt)
        q.Empty() #måste rensa känkade listan
        p.Empty() #måste rensa känkade listan
        main()


if __name__ == '__main__':
	main()

