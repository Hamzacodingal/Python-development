def fact(a):
    if a == 0:
        return True
    return (a*fact(a-1))
print(fact(6))
