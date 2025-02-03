class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Operation (nombre 1 = {self.nombre1}, nombre 2 = {self.nombre2})"
    

# Instanciation de la classe
operation_instance = Operation(12, 5)

# Affichage de l'objet en console
print(operation_instance)
