import timeit

class Song:
    def __init__(self, track_id, låt_id, key_namn, låt_titel):
        self.track_id = track_id
        self.låt_id = låt_id
        self.key_namn = key_namn
        self.låt_titel = låt_titel

    def __lt__(self, other):
        return self.track_id < other.track_id

def readfile(file_name):
    LIST_SONG = []
    DICT_SONG = {} # Dictionary syntax
    with open(file_name, encoding='utf-8') as data_set:
        for raw_row in data_set:
            row = raw_row.strip('\n').split('<SEP>')
            song_object = Song(row[0], row[1], row[2], row[3])
            LIST_SONG.append(song_object)
            DICT_SONG[row[0]] = song_object
    return LIST_SONG, DICT_SONG



'''
Tidskomplexitet O(n)
'''
def linsok(song_list, key):
    # Tagen från föreläsning 3. Har en tidskomplexitet på O(n)
    for x in song_list:
        if key == x.track_id:
            return True
    return False

'''
quicksort och dess hjälpfunktioner togs från föreläsning 7.
Tidskomplexitet på O(n log(n)) i bästa fallet och O(n^2) i värsta fallet
'''
# Använd mergesort istället, finns i föreläsning 7
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and pivot < data[h]:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v


# Tidskomplexitet O(log n)

def binary_search(the_list, key):
   low = 0
   high = len(the_list)-1 # För att kunna komma det sista elementet
   found = False

   while low <= high and not found:
      middle = (low + high)//2
      if the_list[middle] == key:
         found = True
      else:
         if key < the_list[middle]:
            high = middle - 1
         else:
            low = middle + 1
   return found

'''
Tidskomplexitet O(1)
'''
def dictsok(song_dict, key):
    resultat = song_dict[key]

def main():

    filename = "unique_tracks.txt"
    
    lista, dictionary = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testkey = sista.track_id

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testkey), number = 1)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    sorttid = timeit.timeit(stmt = lambda: quicksort(lista), number = 1)
    print("Det tog", round(sorttid, 4), "att sortera listan med hjälp av quicksort")

    bintid = timeit.timeit(stmt = lambda: binary_search(lista, testkey), number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    dicttid = timeit.timeit(stmt = lambda: dictsok(dictionary, testkey), number = 10000)
    print("Uppslagning i dictionary tog", round(dicttid, 4) , "sekunder")

if __name__ == '__main__':
    main()