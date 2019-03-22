# Tildan-Volume-2
def number(q):
    if q.peek() is not None:
        if q.peek().isdigit():
            
            if q.peek() is "0":
                raise Syntaxfel("får ej börja med noll")
            elif q.peek() is  "1":
                 q.dequeue()
                 while q.peek() is not None:
                     if q.peek().isdigit()
                        q.dequeue()
                        pass
                    else:
                        raise Syntaxfel("SyntaxFel")
            else:
                raise Syntaxfel("Siffran måste vara större än 1")
        else:
            raise Syntaxfel("SyntaxFel")
