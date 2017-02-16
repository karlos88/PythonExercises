"""
Python Version: 3
Product Inventory Project - Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""


class Product(object):
    p_id_cnt = 0

    def __init__(self, name, price, quantity=0):
        Product.p_id_cnt += 1
        self.id = Product.p_id_cnt
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return("{self.id} {self.name} {self.price} {self.quantity}".format(self=self))


class Inventory(object):
    inv_id_cnt = 0

    def __init__(self):
        Inventory.inv_id_cnt += 1
        self.id = Inventory.inv_id_cnt
        self.products_list = []

    def add_product(self, name, price, quantity=0):
        self.products_list.append(Product(name, price, quantity))

    def del_product_by_id(self, p_id):
        for product in self.products_list:
            if product.id == p_id:
                self.products_list.remove(product)

    def del_product_by_name(self, name):
        for product in self.products_list:
            if product.name in name:
                self.products_list.remove(product)

    def print_products(self):
        for product in self.products_list:
            print(product)

    def count_inv_value(self):
        return sum(pr.quantity * pr.price for pr in self.products_list)

    def count_product_types(self):
        return len(self.products_list)

    def count_all_products(self):
        return sum(pr.quantity for pr in self.products_list)

if __name__ == "__main__":

    inv = Inventory()

    inv.add_product("Butter", 5, 10)
    inv.add_product("Bread", 1)
    inv.add_product("Duplicate Bread", 3, 10)
    inv.add_product("DELETE", 7, 7)
    inv.add_product("DELETE", 10, 7)

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
