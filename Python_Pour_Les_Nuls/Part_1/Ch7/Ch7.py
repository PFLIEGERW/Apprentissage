# TestMe=6

# if TestMe==6:
#     print("TestMe est égale à 6 !")
#     print("Terminé !")

# Value=int(input("Veuillez entrer un nombre compris entre 1 et 10 : "))
# if (Value > 0) and (Value <= 10):
#     print("Vous avez entré :", Value)
# else:
#     print("Vous avez entré une valeur incorrecte !")

# print("1. Rouge")
# print("2. Orange")
# print("3. Jaune")
# print("4. Vert")
# print("5. Bleu")
# print("6. Pourpre")

# Choice=int(input("Choisissez votre couleur préférée : "))

# if (Choice==1):
#     print("Vous avez choisi Rouge !")
# elif (Choice==2):
#     print("Vous avez choisi Orange !")
# elif (Choice==3):
#     print("Vous avez choisi Jaune !")
# elif (Choice==4):
#     print("Vous avez choisi Vert !")
# elif (Choice==5):
#     print("Vous avez choisi Bleu !")
# elif (Choice==6):
#     print("Vous avez choisi Pourpre !")
# else:
#     print("Vous avez fait un choix invalide !")

# One=int(input("Tapez un nombre entre 1 et 10 : "))
# Two=int(input("Tapez un nombre entre 1 et 10 : "))

# if (One>=1) and (One<=10):
#     if (Two>=1) and (Two<=10):
#         print("Votre nombre secret est : ", One*Two)
#     else:
#         print("La seconde valeur est incorrecte.")
# else:
#     print("La première valeur est incorrecte.")

print("1. Oeufs")
print("2. Crêpes")
print("3. Gauffres")
print("4. Céréales")

MainChoice=int(input("Que voulez vous au petit déjeuner ? "))

if (MainChoice==2):
    Meal="Crêpes"
elif (MainChoice==3):
    Meal="Gaufres"

if (MainChoice==1):
    print("1. Galette au froment")
    print("2. Beignet")
    print("3. Galette de seigle")
    print("4. Crèpes nature")
    Pancake=int(input("Choisissez un type de crèpe : "))

    if (Pancake==1):
        print("Vous avez choisi des oeufs avec une galette au froment.")
    elif (Pancake==2):
        print("Vous avez choisi des oeufs avec des beignets.")
    elif (Pancake==3):
        print("Vous avez choisi des oeufs avec une galette de seigle.")
    elif (Pancake==4):
        print("Vous avez choisi des oeufs avec une crèpe nature.")
    else:
        print("Nous avons des oeufs, mais pas ce type de crèpe.")

elif (MainChoice==2) or (MainChoice==3):
    print("1. Sirop")
    print("2. Confiture de fraises")
    print("3. Sucre en poudre")
    Topping=int(input("Choisissez une garniture : "))

    if (Topping==1):
        print("Vous avez choisi " + Meal + " au sirop.")
    elif (Topping==2):
        print("Vous avez choisi " + Meal +" à la confiture de fraises.")
    elif (Topping==3):
        print("Vous avez choisi " + Meal + " avec du sucre en poudre")
    else:
        print("Nous avons des " + Meal + ", mais pas avec cette garniture.")
elif (MainChoice==4):
    print("Vous avez choisi des céréales.")
else:
    print("Désolé, nous n'avons pas cela dans notre menu !")