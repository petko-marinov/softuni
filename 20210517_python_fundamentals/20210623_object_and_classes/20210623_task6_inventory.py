# Task 6 - Inventory

class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        output_items = ", " .join(self.items)
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {output_items}.\nCapacity left: {left_capacity}"
