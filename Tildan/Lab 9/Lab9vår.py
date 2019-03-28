from linkedQFile import *
import sys
import string
par=[]
q = LinkedQ()

ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V',
  'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se',
   'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 
   'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 
   'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
    'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 
    'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac',
     'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 
     'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
    pass

def readFormel(molekyl): #NY
	"""<formel>::= <mol> \n"""
	q = molecule(molekyl)
	try:
		readMolekyl()
		if len(par) > 0:
			raise Syntaxfel('Saknad högerparentes vid radslutet ')
		return 'Formeln är syntaktiskt korrekt'
	except Syntaxfel as error:
		return str(error) + printQ()

def readMolekyl(): #NY
	"""<mol>   ::= <group> | <group><mol>"""
	"""readmol() anropar readgroup() och sedan eventuellt sej själv
	(men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck)"""

	readGrupp()
	if q.isEmpty():
		return
	elif q.peek() == ")":
		if len(par) < 1:
			raise Syntaxfel("Felaktig gruppstart vid radslutet1 ") 
		return
	else:
		readMolekyl()
def readGrupp(): #Ny
	"""<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
	"""readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol()"""

	if q.isEmpty():
		raise Syntaxfel("Felaktig gruppstart vid radslutet3 ")
	elif q.peek().isdigit():
		raise Syntaxfel("Felaktig gruppstart vid radslutet4 ")

	elif q.peek().isalpha():
		#print("Kallar på readAtom i readGrupp")
		readAtom()
		if q.peek() is None:
			return
		if q.peek().isdigit():
			readNum()
		return

	elif q.peek() == "(":
		par.append(q.dequeue())
		readMolekyl()

		if q.peek() != ")":
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
				

		if q.isEmpty():
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			par.pop()
			q.dequeue()
			if q.isEmpty():
				raise Syntaxfel("Saknad siffra vid radslutet ")
			readNum()
	else:
		raise Syntaxfel("Felaktig gruppstart vid radslutet2 ")


def readAtom(): #NY
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



# Funktion molecule ska lagra alla symboler i en länkad lista
def molecule(indata):
    q = LinkedQ()
    for i in indata:
            q.enqueue(i)
    return q

# Funktion uppercase kontrollerar ifall bokstaven är en stor bokstav
def uppercase(q):
    if q.peek().isupper():
        q.dequeue()
    else:
        raise Syntaxfel("En stor bokstav saknas!")

# Funktion lowercase kontrol
def lowercase(q):
    if q.peek().islower():
        q.dequeue()
        number(q)


# kollar ifall siffer används rätt
def number(q):
    if q.peek() is not None:
        b = q.peek()
        print(b)
        if q.peek().isdigit():
            
            if q.peek() is "0":
                raise Syntaxfel("får ej börja med noll")
            elif q.peek() is  "1":
                q.dequeue()
                if q.peek() is None:
                    raise Syntaxfel("Siffran måste vara större än 1!")

                else:
                    while q.peek() is not None:
                        if q.peek().isdigit():
                            q.dequeue()
                            pass
                        else:
                            raise Syntaxfel("SyntaxFel2")
            elif q.peek().isdigit():
                q.dequeue()
                number(q)

            
            else:
                raise Syntaxfel("Siffran måste vara större än 1")

        elif q.peek().isupper():
            uppercase(q)


        else:
            raise Syntaxfel("SyntaxFel3")
"""
# kollar om molekylen har rätt syntax
def syntax_control(indata):
    q = molecule(indata)
    try:
        readGrupp()
        uppercase(q)
        lowercase(q)
        number(q)
    except Syntaxfel as fel:
        return str(fel)
    return "Formeln följer korrekt syntax!"
"""
def printQ():
	rest = ""
	while not q.isEmpty():
		rest = rest + q.dequeue()
	return rest

def syntax_control(molekyl):
	"""<formel>::= <mol> \n"""
	q = molecule(molekyl)
	try:
		readMolekyl()
		if len(par) > 0:
			raise Syntaxfel('Saknad högerparentes vid radslutet ')
		return 'Formeln är syntaktiskt korrekt'
	except Syntaxfel as error:
		return str(error) + printQ()

def main():
    indata = input("Skriv en molekyl: ").strip() # kolla om den är tom
    resultat = syntax_control(indata)
    print(resultat)

def main2(x): # kolla om den är tom
    resultat = syntax_control(x)
    print(resultat)

x1 = "Na"
x2 = "H2O"
x3 = "Si(C3(COOH)2)4(H2O)7"
x4 = "Na332"

if __name__ == '__main__':
    #main2(x1)
    #main2(x2)
    main2(x3)
    #main2(x4)

        

