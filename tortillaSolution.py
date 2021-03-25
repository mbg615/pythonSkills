from random import randint

def reverse(lst):
    lst.reverse
    return lst

def valFlip(lst):
    for i in lst:
        if lst[i] == 0:
            lst[i] = 1
        if lst[i] == 1:
            lst[i] = 0
    return lst

def main():
     # <------------------ Create List ------------------>
    tortillas_orig = []
    for i in range(10): # Change the range to lengthen the list
        tortillas_orig.append(randint(0,1))
    tortillas_mod = tortillas_orig

    # <------------------ Sorting Code ------------------>
    while not all(i for i in tortillas_mod):
        if tortillas_mod[0] == 0:
            print("Reversing list. . .")
            tortillas_mod = valFlip(reverse(tortillas_mod)) # Flip the values of the reversed list.
    
    # <------------------ End Sequence ------------------>
    print("All tortillas are smiley side up!\nOriginal:", tortillas_orig, "\nCorrected:", tortillas_orig)

    # <------------------ Call Main ------------------>
if __name__ == "__main__":
    main() # Call the main function