class Song:
    def __init__(self, track_id, artistnamn, sångtitel, låtlängd, år):
        # artistid	artistnamn	sångtitel	låtlängd	år   (inläsnings strukturen)
        self.track_id = track_id
        self.artistnamn = artistnamn
        self.sångtitel = sångtitel
        self.låtlängd = låtlängd
        self.är = år



def readfile(file_name):
    LIST_SONG = []
    DICT_SONG = {} # Dictionary syntax
    with open(file_name, encoding='utf-8') as data_set:
        for raw_row in data_set:
            row = raw_row.strip('\n').split('\t')
            song_object = Song(row[0], row[1], row[2], row[3], row[4])
            LIST_SONG.append(song_object)
            DICT_SONG[row[3]] = song_object
    return LIST_SONG, DICT_SONG
        
def nstorsta2(x, n): #x är listan och n är vilket tal vi vill ha
    list1 = []
    for i in range(n):
        list1.append(x.pop(max(x)))
    print(list1[-1].låtlängd)


filename = "testlistan.txt" #behövs sen
lista, dictionary = readfile(filename) #behövs sen


nstorsta2(dictionary,3) 
nstorsta2(dictionary,2)
nstorsta2(dictionary,1)