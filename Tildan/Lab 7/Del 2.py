class HashNode:
    def __init__(self, nyckel, värde):
        self.nyckel = nyckel
        self.värde = värde


class HashTabell:
    def __init_(self, storlek = 32):
        self._storlek = storlek
        self._tabell = [None] * self._storlek
        self._tilläg = 0
"""
    def _getitem__(self, nyckel):
        if key in HashTabell:
            self.get(key)
        else
            KeyError

"""
    def __getitem__(self, nyckel):
        try: 
            self.hämta(key)
        except KeyError
            print("Nyckel finns ej")

    def __putitem__(self, nyckel, value):
        self.put(key, value)
    
    





   
   
   
    def omformatera(self):                       # Done #Funktion som hjälper oss att göra våran Hashtabell större.
        self._table = self._table + [None] * self._size
        self._size = self._size * 2

    def hämta(self, nyckel1):                    #Funktion som hjälper oss att plocka ut de vi eftersöka från vår Hashtabell.
        index = self._hashfunc(nyckel1) #index i hashtabeln
        attempts = 0
        new_index = index - 1
        while attempts <= self._size: # så länge försök är mindre eller lika med storleken
            new_index = (new_index + 1) % self._size
            if self._table[new_index] is not None and self._table[new_index].key == key1:
                return self._table[new_index].value
            attempts += 1
        raise KeyError   


    def _hashfunc(self,key):        #Done #Vår egenskriven hashfunktion som returnerna våra "key's" till Hashtabellen.
        n = len(key)
        keySum = 0 
        for x in range(n):
            keySum = keySum + ord(key[x])
        return keySum%self.size)