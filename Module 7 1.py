from pprint import pprint
class Product():
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
       return(f'{self.name}, {self.weight}, {self.category}')


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):

        file = open(self.__file_name, 'r')
        inf = pprint(self.file.read())
        file.close()
        print(f'{inf}')

    def add(self, *products):
        for a in products:
            self.get_products(a)
            prod = (str(a))
            if prod in self.inf:
                print(f'Продукт {self.prod} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.append(f'{self.prod}\n')
                file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())