class Employee:
    __company = "风云集团"
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def __work(self):
        print("好好学习python,不眠不休")
        print("年龄：{0}".format(self.__age))
        print(Employee.__company)

e = Employee("ruyan",6)
print(e.name)
print(e._Employee__age)
print(dir(e))
e._Employee__work()
e._Employee__work()


class Student:
    company = "风云集团"

    @classmethod
    def printcompany(cls):
        print(cls.company)

Student.printcompany()