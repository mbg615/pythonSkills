from random import randint

def flipList(lst, start):
    store = []
    reversedList = []
    listVal = start
    for i in range(0, start):
        store.append(lst[i])
    while listVal < len(lst) - start:
        reversedList.append(lst[listVal])
        listVal += 1
    for i in store:
        reversedList.append(i)
    reversedList.pop(0)
    i = 0
    while i < len(reversedList):
        if reversedList[i] == 0:
            reversedList[i] = 1 # Changes 0 to 1
            i += 1
            continue
        if reversedList[i] == 1:
            reversedList[i] = 0 # Changes 1 to 0
        i += 1
    combinedList = store + reversedList
    print("Store:", store, "RevList:", reversedList)
    return combinedList

def sort(lst):
    while not all(i for i in lst):
        for i in range(len(lst)-1):
            if lst[i] == 0:
                newLst = flipList(lst, i)
                print(lst)
                print(newLst)
                if all(i for i in newLst):
                    print("Tortilla pile is sorted:", newLst)
                    exit()
    print("Tortilla pile is sorted:", lst)
    exit()
        

def main():
    tortillas = [1, 0, 1, 0, 1]
    # Define list
    '''
    for i in range(0, 10, 1):
        rand = randint(0,1)
        tortillas.append(rand)
        '''
    sort(tortillas)

if __name__ == "__main__":
    main()