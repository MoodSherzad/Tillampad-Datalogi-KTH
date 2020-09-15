from linkedQFile import LinkedQ
from bintreeFile import Bintree
svenska = Bintree()  # Skapar ett binärt sökträd för de svenska orden
gamla = Bintree()  # Skapar ett binärt sökträd för de gamla orden


with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, child):
        if child is not None:
            self.writechain(child.parent)
            print(child.word)
            
            
def makechildren(nod, slutord, q):
    for i in range(len(nod.word)):   # for loop som går igenom rang med ordets storlek ex [0,1,2]
        for letter in "abcdefghijklmnopqrstuvwxyzåäö": # for loop som går igenom varje bokstav
            if nod.word[i] is letter:
                pass
            else:
                if i == 0:
                    new_word = letter + nod.word[1] + nod.word[2]  #nya ordet när vi byter första bokstaven
                elif i == 1:
                    new_word = nod.word[0] + letter + nod.word[2] #nya ordet när vi byter andra bokstaven
                elif i == 2:
                    new_word = nod.word[0] + nod.word[1] + letter  #nya ordet när vi byter tredje bokstaven
                if new_word in svenska and new_word not in gamla:
                    if new_word == slutord:
                        new_child = ParentNode(new_word, nod)
                        print("\n"*3 + "Från startord till slutord: \n")
                        new_child.writechain(new_child)
                        return True                          
                    else:
                        new_child = ParentNode(new_word, nod)
                        q.enqueue(new_child)
                        gamla.put(new_word)

def main():
    start = input("Ange startordet: ")
    slut = input("Ange slutordet: ")
    first_parent = ParentNode(start)
    queue = LinkedQ()
    queue.enqueue(first_parent)
    while not queue.isEmpty():
            nod = queue.dequeue()
            if makechildren(nod, slut, queue) is True:
                print("Det finns en väg till", slut)
                break
            elif queue.isEmpty() is True:
                print("Det finns ingen väg till", slut)

main()

# Det är i princip samma som lab 4, men vi sparar vägen också