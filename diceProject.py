import random
import matplotlib
from colored import fg, attr

run = input("Do you want to roll a die? ")
if run != "no":
    while run != "no":
    
        num = random.randint(1,6)
        red = random.uniform(0.0,1.0)
        green = random.uniform(0.0,1.0)
        blue = random.uniform(0.0,1.0)
    
        rgb = matplotlib.colors.to_hex([ red, green, blue, 1 ], keep_alpha=True)
        color = fg(rgb)
        res = attr('reset')
        print (color + str(num) + res)

        cont = input("Do you want to roll again? ")
        if cont == "no":
            run = "no"      


        
        
