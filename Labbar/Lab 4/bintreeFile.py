class Node: 
    def __init__(self, value): # Varje nod har ett värde och 2 pekare som har varsin riktning
        self.value = value
        self.left = None
        self.right = None


class Bintree: 
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        if self.root is None:
            self.root = Node(newvalue)
        else:
            self.putta(self.root, newvalue)

    def __contains__(self, value):
        return self.finns(self.root, value)

    def write(self):
        self.skriv(self.root)
        print("\n")

    def putta(self, thisNode, value):
        if value < thisNode.value:
            if thisNode.left is None:
                thisNode.left = Node(value)
            else:
                self.putta(thisNode.left, value)
        else:
            if thisNode.right is None:
                thisNode.right = Node(value)
            else:
                self.putta(thisNode.right, value)

    def finns(self, thisNode, value):
        if thisNode is None:
            return False
        elif value == thisNode.value:
            return True
        elif value < thisNode.value:
            return self.finns(thisNode.left, value)
        else: 
            return self.finns(thisNode.right, value)

    def skriv(self, thisNode):
        if thisNode is not None:
            self.skriv(thisNode.left)
            print(thisNode.value)
            self.skriv(thisNode.right)

# kunna rita och berätta hur binärträdet byggs upp,

# visa hur du testat din klass för binära träd,

# förklara varför det går snabbt att söka i ett binärträd 
# För varje sökning så blir listan halverad, tidskomplexiteten är genomsnittligt log n, och i värsta fall är den ordo n

# förklara idén bakom att ha put som anropar putta, etc: 
# Så att man får en smidig rekursiv funktion
# För att man inte kan ha en rekursion inuti i en metod
