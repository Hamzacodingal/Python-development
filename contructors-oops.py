class fruit:
    def __init__(self,weight,name):
        self.weight = weight
        self.name = name
        
opps = fruit(200,"Water melon")
print("weight = ",opps.weight , "Grms","\nname = ",opps.name)

class car:
    def __del__(self):
        print("Deleted")
obj = car()
del obj