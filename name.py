numbers = [1,4,7,8,9]

number2 = []

for i in range(len(numbers)):
    if numbers[i]%2 == 0 :
        print("This is a even number.")
        number2.append(numbers[i])
    else:
        print("Not a even number.")
print(number2)
