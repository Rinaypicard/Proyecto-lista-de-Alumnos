
class alumno:
    name = ''
    lastName = ''
    edad = ''
    cinta = ''

    def __init__(self, name, lastName, age, cinta):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.cinta = cinta
    def getFullName(self):
        return '{0} {1}'.format(self.name, self.lastName)
    def getNameAndAge(self):
        return  '{0} {1}'.format(self.getFullName(), self.age)

    def getAll(self):
        return  '{0} {1}'.format(self.getNameAndAge(), self.cinta)


