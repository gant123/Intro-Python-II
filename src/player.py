# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.current_room = current_room
        self.name = name
        self.inventory = inventory

    def __add_item__(self, item):
        self.inventory.append(item)
        item.on_take()
        return self.inventory

    def __remove_item__(self, idx):
        item = self.inventory.pop(idx)
        item.on_drop()
        return self.inventory

    def pickup_item(self, name):
        item = self.current_room.remove_item(name)
        if item:
            return self.__add_item__(item)
        else:
            return False

    def drop_item(self, name):
        item = None
        item_index = None
        for idx, i in enumerate(self.inventory):
            if i.name.lower() == name:
                item = i
                item_index = idx
                break
        if item:
            self.current_room.add_item(item)
            return self.__remove_item__(item_index)
        else:
            return False

    def inventory_string(self):
        return "\n".join(str(item) for item in self.inventory)
