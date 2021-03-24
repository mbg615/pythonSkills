from random import randint

def main():
     # <------------------ Create List ------------------>
    tortillas_orig = []
    for i in range(10): # Change the range to lengthen the list
        tortillas_orig.append(randint(0,1))

    # <------------------ Sorting Code ------------------>
    while not all(i for i in tortillas_orig):
        print("In loop")
    
    # <------------------ End Sequence ------------------>
    print("All tortillas are smiley side up!\nOriginal:", tortillas_orig, "\nCorrected:", tortillas_orig)

    # <------------------ Call Main ------------------>
if __name__ == "__main__":
    main()