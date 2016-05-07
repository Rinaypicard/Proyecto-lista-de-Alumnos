class Sensei:
    name = ''
    lastName = ''
    edad = ''

    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age
    def getFullName(self):
        return '{0} {1}'.format(self.name, self.lastName)
    def getNameAndAge(self):
        return  '{0} {1}'.format(self.getFullName(), self.age)
class Main:
    yo = Sensei('Rinay', 'Picard', 19)
    print(yo.name)
    print(yo.getFullName())
    print(yo.getNameAndAge())
