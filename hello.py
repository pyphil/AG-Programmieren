class Name():
    def __init__(self, n):
        self.name = n

    def getMessage(self):
        return "Hello" + self.name


print("Hello World!")

m = Name()

print(m.getMessage("john"))
