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

def atom_info():
    """Returnerar en dict med atomernas namn och vikt"""
    vikter = "H  1.00794, He 4.002602, Li 6.941, Be 9.012182, B  10.811, C  12.0107, N  14.0067, O  15.9994, F  18.9984032, Ne 20.1797, \
Na 22.98976928, Mg 24.3050, Al 26.9815386, Si 28.0855, P  30.973762, S  32.065, Cl 35.453, K  39.0983, Ar 39.948, Ca 40.078, Sc 44.955912, \
Ti 47.867, V  50.9415, Cr 51.9961, Mn 54.938045, Fe 55.845, Ni 58.6934, Co 58.933195, Cu 63.546, Zn 65.38, Ga 69.723, Ge 72.64, As 74.92160, \
Se 78.96, Br 79.904, Kr 83.798, Rb 85.4678, Sr 87.62, Y  88.90585, Zr 91.224, Nb 92.90638, Mo 95.96, Tc 98, Ru 101.07, Rh 102.90550, Pd 106.42, \
Ag 107.8682, Cd 112.411, In 114.818, Sn 118.710, Sb 121.760, I  126.90447, Te 127.60, Xe 131.293, Cs 132.9054519, Ba 137.327, La 138.90547, \
Ce 140.116, Pr 140.90765, Nd 144.242, Pm 145, Sm 150.36, Eu 151.964, Gd 157.25, Tb 158.92535, Dy 162.500, Ho 164.93032, Er 167.259, Tm 168.93421, \
Yb 173.054, Lu 174.9668, Hf 178.49, Ta 180.94788, W  183.84, Re 186.207, Os 190.23, Ir 192.217, Pt 195.084, Au 196.966569, Hg 200.59, Tl 204.3833, \
Pb 207.2, Bi 208.98040, Po 209, At 210, Rn 222, Fr 223, Ra 226, Ac 227, Pa 231.03588, Th 232.03806, Np 237, U  238.02891, Am 243, Pu 244, Cm 247, \
Bk 247, Cf 251, Es 252, Fm 257, Md 258, No 259, Lr 262, Rf 265, Db 268, Hs 270, Sg 271, Bh 272, Mt 276, Rg 280, Ds 281, Cn 285"
    vikt_info = vikter.split(", ")

    vikt_info = atom_info()
    print(vikt_info)
    vikt_info = atom_info()
    atom_dict = {}
    for line in vikt_info:
        atom, vikt = line.split()
        atom_dict[atom] = vikt
    return atom_dict


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

def weight


def main():
    
    if input("Vill du testa egen molekyl Y/N: ").strip() in ["Y","y"]:
        in_data = input("Skriv in molekylen du vill testa:  ") # väntar input
    else:
        in_data = "Si(C3(COOH)2)4(H2O)7"
    atom_dict = atom_info()
    print(atom_dict)

    
    mg = Molgrafik()
    if in_data != "q":  # hashtag är en stoppkolss
        p = readFormel(in_data)
        firstError()
        mg.show(p)
        q.Empty() #måste rensa känkade listan
        parantes.Empty() #måste rensa känkade listan
        main()
        


if __name__ == '__main__':
	main()

