# Task 3 - Catalogue

class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        output_list = []
        for j in range(0, len(self.products)):
            if self.products[j][0] == first_letter:
                output_list.append(self.products[j])
        return output_list

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:"
        self.products.sort()
        for i in range(0, len(self.products)):
            output += "\n" + self.products[i]
        return output
