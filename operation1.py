class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition de {self.nombre1} et {self.nombre2} est : {resultat}")

# Instanciation de la classe avec des valeurs spécifiques
operation_instance = Operation(12, 5)

# Appel de la méthode addition pour afficher le résultat
operation_instance.addition()
