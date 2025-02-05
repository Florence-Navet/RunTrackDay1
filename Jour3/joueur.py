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
               pass

        def recevoir_unCartonJaune(self):
                pass

        def recevoir_unCartonRouge(self):
                pass

        def afficher_Statistiques(self):
                pass




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
                

                