class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None




