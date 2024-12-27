print("Here You can Check The numbers is prime or not ")

Check = int(input("Select Any Number From 1 - Infinity::::"))

for i in range (2,Check):
    if Check % i == 0 : 
        print("The Number Is Not A Prime Number:::")
        break
else:
     print("The Number Is A Prime Number:::")