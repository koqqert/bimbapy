#class Robot
class Robot:
    def __init__(self, name = None, age = None, material = None, damage = None, armor = None):
        self.set_data(name, age, material, damage, armor)
        self.data_output()
    def set_data(self, name, age, material, damage, armor):
        self.name = name
        self.age = age
        self.material = material
        self.damage = damage
        self.armor = armor
    def data_output(self):
        print(f'имя: {self.name}, возвраст: {self.age}, материал: {self.material}, урон; {self.damage}, броня: {self.armor}')
robot1 = Robot('оптимус-прайм', 24,'titan', 100, 1000)
robot2 = Robot('бамблби', 12, 'metall', 150, 700)
#class Book
class Book:
    def __init__(self, name, age, author, year, sum_pages = None):
        self.name = name
        self.author = author
        self.year = year
        self.sum_pages = sum_pages
        self.data_output()
    def data_output(self):
        print(f'название: {self.name}, автор: {self.author}, год: {self.year}, кол-во страниц: {self.sum_pages}')
book1 = Book('Война и мир', 65, 'Л.Н.Толстой', 1865, 1000)
book2 = Book('Властелин колец', 50, 'Джон Рональд Руэл Толкин', 1954, 2000)
#class Father
class Father:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.data_output()
    def data_output(self):
        print(f'имя: {self.name}, возвраст: {self.age}')
father1 = Father('вася', 45)
father2 = Father('петя', 35)