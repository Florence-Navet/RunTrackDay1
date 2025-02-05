class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.decription = description
        self.statut = "à faire"



class ListeDeTaches:
    def __init__(self):
        self.taches = []
        

    def ajouter_tache(self, tache):
        if tache not in self.taches:
            self.taches.append(tache)

    def supprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"La {tache} est terminée.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def afficher_liste(self):
        if not self.taches:
            print("Aucune tâche dans la liste.")
        else:
            for tache in self.taches:
                print(tache)
                print("-" * 20)




#Creéation de la liste de tâches
liste = ListeDeTaches()

#Créations des tâches
tache1 = Tache("Finir le Job 3","Pour faire le Job 4")
tache2 = Tache("Faire mon linge", "Allez au lavomatique")
tache3 = Tache("Regarder un drama","Yong Pal")
tache4 = Tache("Appelez Kevin","Pour ce week-end")

#Ajout des taches dans la liste
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)
liste.ajouter_tache(tache4)

#Afficher les taches
print("Toutes les tâches :")
liste.afficher_liste()