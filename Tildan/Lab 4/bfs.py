from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             

def makechildren(startord):
    gamla = Bintree()
    for i in range(len(startord)):
        for letter in "abcdefghijklmnopqrstuvwxyzåäö":
            if startord[i] is letter:
                pass
            else:
                if i == 0:
                    new_word = letter + startord[1] + startord [2]
                    #print(new_word)
                    if new_word in svenska and new_word not in gamla:
                        gamla.put(new_word)
                        print(new_word)
                    else:
                        pass
                elif i == 1:
                    new_word = startord[0] + letter + startord[2]

                    if new_word in svenska and new_word not in gamla:
                        gamla.put(new_word)
                        print(new_word)
                    else:
                        pass
                elif i == 2:
                    new_word = startord[0] + startord[1] + letter

                    if new_word in svenska and new_word not in gamla:
                        gamla.put(new_word)
                        print(new_word)
                    else:
                        pass
                else:
                    pass

def main():
    startord = input("Ange startord: ")
    makechildren(startord)

if __name__ == '__main__':
    main()