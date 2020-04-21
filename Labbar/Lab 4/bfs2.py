from LinkedQfile import LinkedQ
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


def makechildren(nod, slutord, q):
    for i in range(len(nod)):   # for loop som går igenom rang med ordets storlek ex [0,1,2]
        for letter in "abcdefghijklmnopqrstuvwxyzåäö": # for loop som går igenom varje bokstav
            if nod[i] is letter:
                pass
            else:
                if i == 0:
                    new_word = letter + nod[1] + nod [2]  #nya ordet när vi byter första bokstaven
                elif i == 1:
                    new_word = nod[0] + letter + nod[2] #nya ordet när vi byter andra bokstaven
                elif i == 2:
                    new_word = nod[0] + nod[1] + letter  #nya ordet när vi byter tredje bokstaven
                if new_word in svenska and new_word not in gamla:
                    if new_word == slutord:
                        return True                          
                    else:
                        q.enqueue(new_word)
                        gamla.put(new_word)

def main():
    start = input("Ange startordet: ")
    slut = input("Ange slutordet: ")
    queue = LinkedQ()
    queue.enqueue(start)
    while not queue.isEmpty():
            nod = queue.dequeue()
            if makechildren(nod, slut, queue) is True:
                print("Det finns en väg till", slut)
                break
            elif queue.isEmpty() is True:
                print("Det finns ingen väg till", slut)

main()

