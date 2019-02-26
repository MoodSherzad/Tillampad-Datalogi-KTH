class Song:
    def __init__(self, track_id, artistnamn, sångtitel, låtlängd, år):
        self.track_id = track_id
        self.artistnamn = artistnamn
        self.sångtitel = sångtitel
        self.låtlängd = låtlängd
        self.är = år

    def __lt__(self, other):
        return self.track_id < other.track_id
#artistid	artistnamn	sångtitel	låtlängd	år

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
        
def nstorsta2(x, n):
    list1 = []
    for i in range(n):
        list1.append(x.pop(x.index(max(x.sångtid))))
    print(list1[0])


filename = "unique_tracks.txt"
lista, dictionary = readfile(filename)
nstorsta2(lista,3)