class Part:
    def __init__(self, name, material):
        self.name = "Mat"
        self.material = "Bois"

    # def get_name(self):
    #     return self.name

    # def get_material(self):
    #     return self.material

    # def set_material(self):
    #     return self.material

    # def set_name(self, name):
    #     self.name = name

    def change_material(self, material):
        self.material = material

    def __str__(self):
        return (f"La pièce {self.name} est fabriquée en {self.material}.")


class Ship(Part):
    def __init__(self, name, material, parts):
        super().__init__(name, material)
        self.__parts = {part.name for part in parts}

    # def get__parts(self):
    #     return self.__parts

    # def set__parts(self, __parts):
    #     self.__parts = __parts

    def display_state(self):
        for part in self.__parts:
            values():
            print(part)

    def replace_part(self, part_name, new_part):
        self.part_name = part_name
        self.__parts[name] = new_part
        return self.__parts
