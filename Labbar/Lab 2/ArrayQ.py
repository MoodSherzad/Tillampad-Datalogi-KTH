from array import array


class ArrayQ:

    def __init__(self):
        self.__deck = array('b')  # "b" bestämmer vad vad som ska matas in

    def enqueue(self, x):
        self.__deck.append(x)  # lägger till i slutet av listan

    def dequeue(self):
        return self.__deck.pop(0)  # plockar ut den första i listan

    def isEmpty(self):
        return len(self.__deck) == 0  # kollar om listan är tom

    def printArray(self):
        print(self.__deck)





