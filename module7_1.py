class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        str_ = file.read()
        file.close()
        return str_

    def add(self, *products):
        self.file_append = open(self.__file_name, 'a')
        for product in products:
            if product.name not in self.get_products():
                self.file_append.write(str(product) + '\n')
                self.file_append.seek(0)
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        self.file_append.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
