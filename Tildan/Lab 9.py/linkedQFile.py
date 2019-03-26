class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, x):
        temp = Node(x)

        if self.first is None:  # fix för första elementet
            self.first = temp
            self.last = temp
        else:
            self.last.next = temp    # den sista nodens pekare ändras från sig själv till den nya noden
            self.last = temp     # den nya noden placeras sist

    def dequeue(self):
        x = self.first.value    # ettan sparas till en variabel
        self.first = self.first.next    # tvåan flyttas fram och blir ettan
        return x

    def isEmpty(self):  # kollar om listan är tom
        return self.first is None     # is snabbare än ==

    def peek(self):

        if self.isEmpty() is False:
            return self.first.value
        else:
            return None

