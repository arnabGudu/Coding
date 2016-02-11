class Animal:
    legs = 4    #class var
    voice = ""
    def __init__(self, name, sound):
        self.voice = sound
        print(name + " " + sound)
    def show(self):
        print(self.name)

cat = Animal("Cat","Mew")
print(cat.show())

