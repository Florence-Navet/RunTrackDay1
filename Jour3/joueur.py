class Joueur:
        def __init__(self, nom_joueur, numero, position, buts_marqués, passes_decisives, cartons_jaunes, cartons_rouges):
                self.nom_joueur = nom_joueur
                self.numero = numero
                self.position = position
                self.passes_decisives = passes_decisives
                self.buts_marqués = buts_marqués
                self.cartons_jaunes = cartons_jaunes
                self.cartons_rouges = cartons_rouges

        def maquer_but(self):
                self.buts_marqués += 1

        def recevoir_unCartonJaune(self):
                self.passes_decisives += 1

        def recevoir_unCartonRouge(self):
                self.cartons_rouges += 1

        def afficher_Statistiques(self):
                self.cartons_jaunes += 1

        def afficher_statistiques(self):
                print(f"Nom: {self.nom_joueur}, Numéro: {self.numero}, Position: {self.position}")
                print(f"Buts marqués: {self.buts_marqués}, Passes décisives: {self.passes_decisives}")
                print(f"Cartons jaunes: {self.cartons_jaunes}, Cartons rouges")




class equipe_de_foot:
        def __init__(self, nom_equipe, liste_joueurs):
                self.nom_equipe = nom_equipe
                self.liste_joueurs = []
        def ajouter_joueur(self, nom_joueur):
                if not nom_joueur in self.liste_joueurs:
                       self.liste_joueurs.append(nom_joueur)
                       print(f"Le joueur {nom_joueur} a été selectionné dans l'équipe {self.nom_equipe}")
                else:
                        print("Ce joueur est déjà dans l'équipe !!")

      
                

     			# Création de joueurs
joueur1 = Joueur("Kevin Mousquet", 9, "Gardien")
joueur2 = Joueur("Quentin Mousquet", 7, "Attaquant")
joueur3 = Joueur("Julien Mousquet", 5, "Défenseur")           
joueur4 = Joueur("Tristan Mousquet", 10, "Milieu")           

   # Affichage initial des statistiques des joueurs
joueur1.afficher_statistiques_joueurs()             