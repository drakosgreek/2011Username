import random


words = ["blocks", "banana", "cherry", "date", "elderberry"]
symbols = ["@", "-", "+-"]
random_addons = ["C0", "L2", "H1"]
addons = random.choice(random_addons)
username_words = random.choice(words)
username_numeric = random.randint(1, 10000)  # numeric range, so e.g block9403, cherry3901
username_symbols = random.choice(symbols)
addons = input("Extra addons? y/n >>>  ")
if addons == "y":
   print(f"{username_words}{username_numeric}{username_symbols}{addons}")
   
elif addons == "n":
   print(f"{username_words}{username_numeric}{username_symbols}") 
   print("Generated username")