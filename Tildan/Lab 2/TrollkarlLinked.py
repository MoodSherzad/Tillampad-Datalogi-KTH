from LinkedQfile import LinkedQ
import sys


def main():

    choice = input("Write N to insert a number or write R to run the wizard: ")
    if choice == "N" or choice == "n":
        number = str(input("Skriv ordningen av korten"))
        number = number.split()
    elif choice == "R" or choice == "r":
        number = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]
    else:
        sys.exit("Bye Felicia")

    for i in range(len(number)):
        number[i] = int(number[i])

    q = LinkedQ()  # Skapar en tom kö
    for x in number:  # Sätter in alla värden i kön
        q.enqueue(x)

    newlist = []
    while q.isEmpty() is False:
        a = q.dequeue()
        q.enqueue(a)
        b = q.dequeue()
        newlist.append(b)
    print(newlist)
main()
