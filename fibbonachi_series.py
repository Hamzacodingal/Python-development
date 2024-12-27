a = 0
b=1
c =[a,b]
num = int(input("How Many times you want the fibbonachi series"))
for i in range(num-2):
    d = a+b
    c.append(d)
    a,b= b,d
print(c)