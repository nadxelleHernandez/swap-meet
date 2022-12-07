class Vendor:
    def __init__(self, inventory = None) :
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        if not item:
            return item

        if item not in self.inventory:
            self.inventory.append(item)
        
        return item

    def remove(self, item):  
        if not item:
            return item

        if item not in self.inventory:
            return None

        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

        return None

    def get_by_category(self, category):
        if not category: 
            return []

        list_by_cate = [item for item in self.inventory if item.get_category() == category]
    
        return list_by_cate 

    def get_best_by_category(self, category):
        items_by_cate = self.get_by_category(category)

        if not items_by_cate:
            return None

        best_item = max(items_by_cate, key = lambda item: item.condition)
        return best_item

    def swap_items(self, other_vendor, my_item, their_item):
        if other_vendor is None or my_item is None or their_item is None:
            return False

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.add(their_item)
        other_vendor.add(my_item)
        self.remove(my_item)
        other_vendor.remove(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        return self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not my_priority or not their_priority:
            return False

        my_interest_item = other_vendor.get_best_by_category(my_priority)
        their_interest_item = self.get_best_by_category(their_priority)

        if not my_interest_item or not their_interest_item:
            return False

        return self.swap_items(other_vendor,their_interest_item,my_interest_item)

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        return self.swap_items(other_vendor,my_item,their_item)
        
    def display_inventory(self, category=""):
        display_items = self.get_by_category(category) if category else self.inventory
        
        if not display_items:
            print("No inventory to display.")
            return

        for i in range(len(display_items)):
            print(f"{i+1}. {display_items[i]}")

    def choose_and_swap_items(self, other_vendor, category=""):
        print("My items:")
        self.display_inventory(category)
        print("\nTheir items:")
        other_vendor.display_inventory(category)

        #add code to prevent exceptions when receiving non int ids
        my_item_id = int(input("Provide the id of the item you want swap: "))
        their_item_id = int(input("Provide the id of the item they want to swap: "))

        return self.swap_by_id(other_vendor,my_item_id,their_item_id)


