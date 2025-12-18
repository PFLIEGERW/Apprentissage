def linear_search(target):
    names = ["Elizabeth", "Samuel", "Jawwad",\
    "Yacoub", "Cara", "Jess",\
    "Benji", "Thamber", "Suki", "Zi", "Q"]
    
    found = False
    
    for count in range(len(names)):
        if target == (names[count]):
        print(target, "found at position", count)
        found = True
    if found == False:
    print(target, "was not found")

name = input("Who are you looking for? ")
linear_search(name)