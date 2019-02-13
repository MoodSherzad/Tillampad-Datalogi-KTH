from ArrayQ import ArrayQ


def main():
    choice = input("Write N to insert a number or write R to run the wizard: ")
    if choice == "N" or choice == "n":
        number = str(input("Skriv ordningen av korten"))
        number = number.split()
    elif choice == "R" or choice == "r":
        number = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]
    else:
        quit
    for i in range(len(number)):
        number[i] = int(number[i])
    queue = ArrayQ()
    newlist = ArrayQ()
    for x in number:  # lägger in korten i objektet
        queue.enqueue(x)

    while queue.isEmpty() is False:
        a = queue.dequeue()
        queue.enqueue(a)
        b = queue.dequeue()
        newlist.enqueue(b)
    print(newlist.printArray())

main()