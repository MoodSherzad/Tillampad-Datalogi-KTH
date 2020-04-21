import timeit
class DictHash:
    def __init__(self):
        self.dict = {}

    def __getitem__(self, nyckel):
        return self.dict[nyckel]

    def lagra(self, nyckel, värde):
        self.dict[nyckel] = värde

class Song:
    def __init__(self, trackid, artistnamn, sångtitel, låtlängd, år):
        # artistid	artistnamn	sångtitel	låtlängd	år   (inläsnings strukturen)
        self.trackid = trackid
        self.artistnamn = artistnamn
        self.sångtitel = sångtitel
        self.låtlängd = låtlängd
        self.är = år

def readfile(fil, n): 
    with open(fil, encoding='utf-8') as text:
        for r in text:
            rad = r.strip('\n').split('\t')
            song = Song(rad[0], rad[1], rad[2], rad[3], rad[4])
            hashtabell.lagra(rad[0], song)
            if n < len(hashtabell.dict):
                break

hashtabell = DictHash()
def main():
    fil = "sang-artist-data.txt"
    readfile(fil, 999987) #999987 #lisstorlek
    tid_dict = timeit.timeit(stmt = lambda: hashtabell["AR30R5E1187B9AD78A"], number = 1)
    print("Det tog", round(tid_dict, 40), "sekunder att slå upp det i dictionary")
    print(hashtabell["AR30R5E1187B9AD78A"].artistnamn)

if __name__ == '__main__':
    main()

# Nej det tar dubbelt så långt tid som att indexa