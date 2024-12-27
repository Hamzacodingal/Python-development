class Robot:
    def introduce(self, name, age):
        print("I am", name, "and I am", age, "years old.")

tom = Robot()
jerry = Robot()

tom.introduce("Tom", 5)
jerry.introduce("Jerry", 3)
