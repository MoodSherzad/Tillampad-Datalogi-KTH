from linkedQFile import *
import sys
import string

q = LinkedQ()
p = LinkedQ()

par=[]

ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


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
	"""readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol()"""

	if q.isEmpty():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")
	if q.peek().isdigit():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

	if q.peek().isalpha():
		#print("Kallar på readAtom i readGrupp")
		readAtom()
		if q.peek() is None:
			return
		if q.peek().isdigit():
			readNum()
		return

	elif q.peek() == "(":
		temp = q.dequeue()
		par.append(temp)
		p.enqueue(temp) #PATANTESER
		readMolekyl()

		if q.peek() != ")":
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
				

		if q.isEmpty():
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			par.pop()
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
		x = q.dequeue()
		#print(x, "readAtom stor bokstav")
	else:
		raise Syntaxfel("Saknad stor bokstav vid radslutet ")

	if q.peek() != None:
		if q.peek().islower():
			x = x + q.dequeue()
			#print("Atomen är", x)
	
	if x in ATOMER:
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


z1 = ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332","C(Xx4)5","C(OH4)C","C(OH4C","H2O)Fe", "H02C", "Nacl","(Cl)2)3"]
z2 = ["Si(C3(COOH)2)4(H2O)7"]
def main():
    for i in z2:
        indata = i
        resultat = readFormel(indata)
        print(resultat)

    if p.isEmpty():
        print("Parantefunktion fungerara")

if __name__ == '__main__':
    main()




