class Joueur:
    def __init__(self, nom_joueur, numero, position, buts_marqués=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        self.nom_joueur = nom_joueur
        self.numero = numero
        self.position = position
        self.buts_marqués = buts_marqués
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges



    def marquer_but(self):
        self.buts_marqués += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiquesJoueur(self):
        print(f"Nom: {self.nom_joueur}, Numéro: {self.numero}, Position: {self.position}")
        print(f"Buts marqués: {self.buts_marqués}, Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}")

    def __str__(self):
        return f"{self.nom_joueur} (#{self.numero}, {self.position})"

class EquipeDeFoot:
        def __init__(self, nom_equipe, liste_joueurs = None):
                self.nom_equipe = nom_equipe
                self.liste_joueurs = []

        def ajouter_joueur(self, nom_joueur):
                if not nom_joueur in self.liste_joueurs:
                       self.liste_joueurs.append(nom_joueur)
                       print(f"Le joueur {nom_joueur} a été selectionné dans l'équipe {self.nom_equipe}")
                else:
                        print("Ce joueur est déjà dans l'équipe !!")  

        def afficher_statisques_des_joueurs(self):
             print(f"Statistiques des joueurs de l'équipe {self.nom_equipe} :") 
             for joueur in self.liste_joueurs:
                  f"{joueur.afficher_statistiquesJoueur()}\n"
                #   print("" * 4)

      
                
         

# Création de joueurs
joueur1 = Joueur("Kevin Mousquet", 9, "Gardien")
joueur2 = Joueur("Quentin Mousquet", 7, "Attaquant")
joueur3 = Joueur("Julien Mousquet", 5, "Défenseur")           
joueur4 = Joueur("Tristan Mousquet", 10, "Milieu")           

equipe = EquipeDeFoot("Les Mousquetaires")
equipe.ajouter_joueur(joueur1)
equipe.ajouter_joueur(joueur2)
equipe.ajouter_joueur(joueur3)
equipe.ajouter_joueur(joueur4)


   # Affichage initial des statistiques des joueurs
joueur1.afficher_statistiquesJoueur()  

#simuler un match
joueur1.recevoir_un_carton_jaune()
joueur4.effectuer_une_passe_decisive()
joueur3.effectuer_une_passe_decisive()
joueur2.marquer_but()

# #affichages statistiques des joueurs
equipe.afficher_statisques_des_joueurs()