"""
Python Version: 3
Product Inventory Project - Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""


class Product(object):
    def __init__(self, p_id, name, price, quantity=0):
        self._id = p_id
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity


class Inventory(object):
    def __init__(self, i_id):
        self._inv_id = i_id
        self._product_list = []
        self._inv_value = 0

    def add_product(self, p_id, name, price, quantity=0):
        self._product_list.append(Product(p_id, name, price, quantity))

    def del_product_by_id(self, p_id):
        for product in self.products:
            if product.id == p_id:
                self.products.remove(product)

    def del_product_by_name(self, name):
        for product in self.products:
            if product.name in name:
                self.products.remove(product)

    def print_products(self):
        for product in self.products:
            print("{p_name} {p_id} {p_price} {p_quantity}".format(
                p_name=product.name, p_id=product.id,
                p_price=product.price, p_quantity=product.quantity
            ))

    def count_inv_value(self):
        value = 0
        for pr in self.products:
            value += pr.quantity * pr.price
        return value
        # Other way:
        # return sum([pr.quantity * pr.price for pr in self.products])

    def count_product_types(self):
        return len(self.products)

    def count_all_products(self):
        return sum([pr.quantity for pr in self.products])

    @property
    def products(self):
        return self._product_list

if __name__ == "__main__":

    inv = Inventory(1)

    inv.add_product(1, "Butter", 5, 10)
    inv.add_product(2, "Bread", 1)
    inv.add_product(2, "Duplicate Bread", 3, 10)
    inv.add_product(4, "DELETE", 7, 7)
    inv.add_product(5, "DELETE", 7, 7)

    print("Products list:")
    inv.print_products()
    print("No. of product types: {}".format(inv.count_product_types()))
    print("No. of all products: {}".format(inv.count_all_products()))
    print("Total inventory value: {}".format(inv.count_inv_value()))

    print("---------------\n")
    inv.del_product_by_id(4)
    inv.print_products()

    print("---------------\n")
    inv.del_product_by_name("DELETE")
    inv.print_products()
