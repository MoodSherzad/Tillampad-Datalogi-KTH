from bintreeFile import Bintree


svenska = Bintree()
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()               
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)             
print("\n")

engelska = Bintree()
with open("engelska.txt", "r", encoding="utf-8") as engelskfil:
    for rad in engelskfil:
        rad = rad.strip().split()
        for ordet in rad:
            if ordet in engelska:
                pass
            else:
                engelska.put(ordet)
                if ordet in svenska:
                    print(ordet, end=" ")
print("\n")
