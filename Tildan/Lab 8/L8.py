from linkedQFile import *

class Syntaxfel(Exception):
    pass

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


"""def number(q):
    if q.peek() is not None:
        if q.peek().isdigit():
            if q.peek() not in  ["1","0"]:
                q.dequeue()
            else:
                raise Syntaxfel("Siffran måste vara större än 1!")
        else:
            raise Syntaxfel("SyntaxFel")

    """
# kollar ifall siffer används rätt
def number(q):
    if q.peek() is not None:
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
                            raise Syntaxfel("SyntaxFel")
            elif q.peek().isdigit():
                q.dequeue()
                number(q)
            else:
                raise Syntaxfel("Siffran måste vara större än 1")
        else:
            raise Syntaxfel("SyntaxFel")

# kollar om molekylen har rätt syntax
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
    indata = input("Skriv en molekyl: ").strip() # kolla om den är tom
    resultat = syntax_control(indata)
    print(resultat)
    
if __name__ == '__main__':
    main()


        

# Godkänd av Caroline Yu

# Tjena Alexander och Julia