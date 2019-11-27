class Cat:
    name = "None"
    weight = 10
    height = 50

    def put(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
Pet = Cat()
Pet.put("Chip", 5, 30)
if Pet.weight<5 & Pet.height<30:
    print(Pet.name+" "+"small")
elif Pet.weight>=5 & Pet.weight<= 10:
    print(Pet.name+" "+"normal")
else:
    print(Pet.name+" "+"fatty")
class Catsy(Cat):
    nails = "None"
    def __init__(self, name, weight, nails):
        self.name = name
        self.weight = weight
        print(self.name, self.weight, self.nails)
Catsy("Mike", 2,"")
