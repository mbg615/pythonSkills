from random import randint

def flipList(lst, start):
    store = []
    reversedList = []
    listVal = start

    for i in range(0, start):
        store.append(lst[i])
    #if not store:
    #    store.append(list[0])

    while listVal < len(lst) - start + 1:
        reversedList.append(lst[listVal])
        listVal += 1

    for i in store:
        reversedList.append(i)

    i = 0
    while i < len(reversedList):
        if reversedList[i] == 0:
            reversedList[i] = 1
            i += 1
            continue
        if reversedList[i] == 1:
            reversedList[i] = 0
        i += 1

    combinedList = store + reversedList
    print("Store:", store, "RevList:", reversedList, "ComList:", combinedList)
    return combinedList

def sort(lst):
    if all(i for i in lst):
        print("Tortilla pile is already sorted:", lst)
        exit()
    newList = lst
    while not all(i for i in newList): # and len(lst) == len(newList):
        passVal = newList.index(0)
        newList = flipList(newList, passVal)
        if all(i for i in newList):
            print("Tortilla pile", lst, "is sorted:", newList)
            exit()
    print("quited")
    exit()
        

def main():
    tortillas = [1, 1, 1, 0, 1]
    #tortillas = []
    #for i in range(0, 10, 1):
    #    rand = randint(0,1)
    #    tortillas.append(rand)
    sort(tortillas)

if __name__ == "__main__":
    main()