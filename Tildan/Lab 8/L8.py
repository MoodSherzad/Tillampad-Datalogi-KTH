from linkedQFile import *

class Syntaxfel(Exception):
    pass

def Molecule(Molecule):
    q = LinkedQ()
    for i in Molecule:
        q.enqueue(i)
    try:
        uppercase(q)
    except Syntaxfel as fel:
        return str(fel)
    return "Formeln är syntaktiskt korrekt"

def uppercase(q):
    if q.peek().isupper():
        q.dequeue()
        lowercase(q)
        number(q)
    else:
        raise Syntaxfel("Saknar stor bokstav")


def lowercase(q):
    if q.peek().islower():
        q.dequeue()
        number(q)

def number(q):
    if q.peek() is not None:
        if q.peek().isdigit():
            if q.peek() not in  ["1","0"]:
                q.dequeue()
            else:
                raise Syntaxfel("Måste vara större en 2")
        else:
            raise Syntaxfel("SyntaxFel")

def main():
    Molecule = input("Skriv en Molecule: ").strip()
    resultat = Molecule(Molecule)
    print(resultat)
    

if __name__ == '__main__':
    while True:
        main()


        