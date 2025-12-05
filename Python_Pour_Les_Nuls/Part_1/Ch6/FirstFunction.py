#def Hello() :
#    print ("Ceci est ma première fonction python !")
#
#Hello()
#Variable = 5+2
#
#def Hello2( Variable ):
#    print(Variable)
#Hello2(Variable)

# def AddIt (Value1, Value2):
#     print(Value1, "+", Value2, "=", (Value1 + Value2))

# AddIt(Value2=3,Value1=2)

# def Hello3(d, /, Greeting, *, f = "Test f"):
#     print (Greeting)
#     print (d)
#     print(f)

# Hello3(3, "T", f="Test ff")

# def Hello4 (ArgCount, *VarArgs):
#     print("Vous avez passé", ArgCount, "argument(s).")
#     for Arg in VarArgs:
#         print(Arg)
# Hello4(3, 4, 5, 7)

# def DoAdd (Value1, Value2):
#     return Value1 + Value2
# print ("3 + 4 égale 2 + 5 est :", (DoAdd (3, 4) == DoAdd (2, 5)))

Name=input("Quel est votre nom ? : ")
print("Bonjour ", Name)
Age=int(input("Quel est votre age ? "))
print("Vous avez", Age, "an(s)")