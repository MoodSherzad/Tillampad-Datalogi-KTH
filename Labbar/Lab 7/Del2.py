class HashNode:
	def __init__(self, nyckel, data, pekare = None):
		self.nyckel = nyckel
		self.data = data
		self.pekare = pekare # möjliggör länkad lista

	def __str__(self): # den skriver ut shittet
		if self.nyckel != None and self.data != None:
			return "Med nyckel: " + str(self.nyckel) + " får vi värdet " + str(self.data)
		else:
			return None


class Hashtabell:
	def __init__(self, storlek):
		self.storlek = storlek 
		self.platser = [None] * self.storlek
		self.krockar = 0

    # Från föreläsning

	def hashfunk(self, nyckel):
		start = 0
		for i in nyckel[::-1]:
			start = start*2000 + ord(i)
			# start = start*64 + ord(i)
		return start%self.storlek

	def addera(self, nyckel, data): # hanterar krockar
		i = self.hashfunk(nyckel)
		if self.platser[i] is None:
			self.platser[i] = HashNode(nyckel, data)
		else:
			self.krockar += 1
			krock = self.platser[i]
			self.platser[i] = HashNode(nyckel, data)
			self.platser[i].pekare = krock

	def sök(self, nyckel):
		i = self.hashfunk(nyckel)
		nod = self.platser[i]

		while nod is not None:
			if nod.nyckel == nyckel:
				return nod
			nod = nod.pekare
		raise KeyError

def readfile(fil, a ): 
    with open(fil, encoding='utf-8') as text:
        for r in text:
            rad = r.strip('\n').split('\t')
            a.addera(rad[2], rad[1])


def main():
    fil = "sang-artist-data.txt" #"unique_tracks.txt" 
    a = Hashtabell(3000017)
    readfile(fil, a) # 999987
    print(a.sök("Deserve")) # TRNTAUZ128F149BA49 ARS5DE71187B99A194
    print("Antal krockar:", a.krockar)

if __name__ == '__main__':
	main()

	# hashning funkar som en dictionary