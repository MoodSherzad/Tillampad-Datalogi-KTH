from linkedQFile import *

import string

q = LinkedQ()
p = LinkedQ()

atomLista = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
	pass


def storeMolekyl(molekyl):
	"""Lägger in strängen i kön"""
	for symbol in molekyl:
		q.enqueue(symbol)
	return q

def readMolekyl():
	"""<mol>   ::= <group> | <group><mol>"""
	readGrupp()
	if q.isEmpty():
		return
	elif q.peek() is ")":
		if p.isEmpty():
			raise Syntaxfel("Felaktig gruppstart vid radslutet ") 
		return
	else:
		readMolekyl()


def readGrupp():
	"""<group> ::= <atom> |<atom><num> | (<mol>) <num>"""

	if q.isEmpty():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")
	if q.peek().isdigit():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

	if q.peek().isalpha():
		readAtom()
		if q.peek() is None:
			return
		if q.peek().isdigit():
			readNum()
		return

	elif q.peek() is "(": #PATANTESER
		p.enqueue(q.dequeue())
		readMolekyl()
		if not q.peek() is ")":
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
				

		if q.isEmpty():
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			p.dequeue()
			q.dequeue() #PARANTESER
			if q.isEmpty():
				raise Syntaxfel("Saknad siffra vid radslutet ")
			readNum()

			
	else:
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

def readAtom():
	"""<atom>  ::= <LETTER> | <LETTER><letter>"""
	if q.peek().isupper():
		atom = q.dequeue()
		#print(r, "readAtom stor bokstav")
	else:
		raise Syntaxfel("Saknad stor bokstav vid radslutet ")
	if not q.peek() is None:
		if q.peek().islower():
			atom = atom + q.dequeue()
	if atom in atomLista:
		return
	else:
		raise Syntaxfel("Okänd atom vid radslutet ")


def readNum(): #FIXAD DELUX
    if q.peek().isdigit():
        if q.peek() == "0":
            q.dequeue()
            raise Syntaxfel("För litet tal vid radslutet ")
        elif q.peek() == "1":
            q.dequeue()
            if q.peek().isdigit():
                pass
            else:
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
	"""<formel>::= <mol> \n"""
	q = storeMolekyl(molekyl)
	try:
		readMolekyl()
		if p.isEmpty is False:
			raise Syntaxfel('Saknad högerparentes vid radslutet ')
		return 'Formeln är syntaktiskt korrekt'
	except Syntaxfel as error:
		return str(error) + firstError()


def main():
    for i in ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332","C(Xx4)5","C(OH4)C","C(OH4C","H2O)Fe", "H02C", "Nacl","(Cl)2)3"]:
        resultat = readFormel(i)
        print(resultat)

if __name__ == '__main__':
    main()




