from linkedQFile import *

class Syntaxfel(Exception):
    pass


def molecule(indata):
    q = LinkedQ()
    for i in indata:
            q.enqueue(i)
    return q

def uppercase(q):
    if q.peek().isupper():
        q.dequeue()
    else:
        raise Syntaxfel("En stor bokstav saknas")

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
                raise Syntaxfel("Siffran måste vara större än 1")
        else:
            raise Syntaxfel("SyntaxFel")

def syntax_control(indata):
    q = molecule(indata)
    try:
        uppercase(q)
        lowercase(q)
        number(q)
    except Syntaxfel as fel:
        return str(fel)
    return "Formeln följer korrekt syntax!"

def main():
    indata = input("Skriv en molekyl: ").strip()
    resultat = syntax_control(indata)
    print(resultat)
    
if __name__ == '__main__':
    main()


        