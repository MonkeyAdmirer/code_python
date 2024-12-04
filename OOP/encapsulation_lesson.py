class Person:
    def __init__(self, name, wealth):
        self.name = name
        self.__wealth = wealth

    def info(self):
        return f"Person(name: {self.name}, wealth: {self.__wealth})"

    # For encapsulated attributes, if you want to "read" them
    # create a getter method
    # def get_wealth() this is fine
    # @property is a decorator. If not, would have to use print(p1.wealth()). 

    @property
    def wealth(self):
        return self.__wealth

        # setter --> a controlled way to modify an encapsulated attribute
    @wealth.setter
    def wealth(self, new_value):
        self.__wealth = new_value

p1 = Person("Mr. Park", 69)
p2 = Person("Marshall", 100000)
print(p1.wealth)
p1.wealth = 1234
print(p1.info())
