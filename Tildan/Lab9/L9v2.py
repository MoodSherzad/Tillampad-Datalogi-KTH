from linkedQFile import *
import string
import sys
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

class Syntaxfel(Exception):
	pass

def storeMolekyl(molekyl):
	for symbol in molekyl:
		q.enqueue(symbol)
	return q

def readmol():

	readgroup()
	if q.isEmpty():
		return
	elif q.peek() is ")":
		if p.isEmpty():
			raise Syntaxfel("Felaktig gruppstart vid radslutet ") 
		return
	else:
		readmol()

def readgroup():
	if q.isEmpty():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")
	if q.peek().isdigit():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

	if q.peek().isalpha():
		readAtom()
		if q.peek() is None:
			return
		if q.peek().isdigit():
			number()
		return

	elif q.peek() is "(": #PATANTESER
		p.enqueue(q.dequeue())
		readmol()
		if not q.peek() is ")":
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
				

		if q.isEmpty():
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			p.dequeue()
			q.dequeue() #PARANTESER
			if q.isEmpty():
				raise Syntaxfel("Saknad siffra vid radslutet ")
			number()			
	else:
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

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
		return
	else:
		raise Syntaxfel("Okänd atom vid radslutet ")

def number(): #FIXAD DELUX
    if q.peek().isdigit():
        if q.peek() == "0":
            q.dequeue()
            raise Syntaxfel("För litet tal vid radslutet ")
        elif q.peek() == "1":
            q.dequeue()
            #if q.peek().isdigit():
            #    pass
            #else:
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
	q = storeMolekyl(molekyl)
	try:
		readmol()
		if p.isEmpty is False:
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
		return "Formeln är syntaktiskt korrekt"
	except Syntaxfel as error:
		return str(error) + firstError()
"""
def main():
    for i in ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332","C(Xx4)5","C(OH4)C","C(OH4C","H2O)Fe", "H02C", "Nacl","(Cl)2)3"]:
        output = readFormel(i)
        print(output)
"""


def main():
	kattisInput = sys.stdin.readline().strip()
	if kattisInput != "#":  # hashtag är en stoppkolss
		output = readFormel(kattisInput)
		firstError()
		print(output)
		q.Empty() #måste rensa känkade listan
		p.Empty() #måste rensa känkade listan
		main()

def main1():
	for molekyl in ["H2O)Fe", "(Cl)2)3"]:
		if not molekyl is "#":
			output = readFormel(molekyl)
			firstError()
			print(output)

def main2(x):
	q.Empty()
	p.Empty()
	output = readFormel(x)
	firstError()
	return output

if __name__ == '__main__':
    main()




