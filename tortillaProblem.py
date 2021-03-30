from random import randint

def reverse(lst, start):
    listVal = start
    reversedList = []
    for i in range(start, len(lst)):
        reversedList.append(lst[listVal])
        listVal += 1
    return reversedList


def flipList(lst, start):
    lst = reverse(lst, start)
    for j in lst:
                if j == 0:
                    lst[j] = 1
                if j == 1:
                    lst[j] = 0
    return lst

def sort(lst):
    while not all(i for i in lst):
        for i in range(len(lst)):
            if lst[i] == 0:
                lst = flipList(lst, i)
    print("Tortilla pile is sorted:", lst)
        

def main():
    tortillas = [] 
    for i in range(0, 10, 1):
        rand = randint(0,1)
        tortillas.append(rand)
    print(type(tortillas))
    sort(tortillas)

if __name__ == "__main__":
    main()