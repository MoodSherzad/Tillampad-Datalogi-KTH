class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, x):
        temp = Node(x)

        if self.__first is None:  # fix för första elementet
            self.__first = temp
            self.__last = temp
        else:
            self.__last.next = temp    # den sista nodens pekare ändras från sig själv till den nya noden
            self.__last = temp     # den nya noden placeras sist

    def dequeue(self):
        x = self.__first.value    # ettan sparas till en variabel
        self.__first = self.__first.next    # tvåan flyttas fram och blir ettan
        return x

    def isEmpty(self):  # kollar om listan är tom
        return self.__first is None     # is snabbare än ==

    def visa(self):
        return self.value
    def peek(self):

        if self.isEmpty() is False:
            return self.__first.value
        else:
            return None
