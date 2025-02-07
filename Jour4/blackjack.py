import random

class Carte:
    def __init__(self, valeur):
        self.valeur = valeur

    def __str__(self):
        return str(self.valeur)  # Retourner la valeur sous forme de chaîne

class Jeu:
    def __init__(self):
        self.paquet = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, "V", "D", "R", "A", "V", "D", "R", "A", "V", "D", "R", "A", "V", "D", "R", "A"]
        self.main_joueur = []
        self.main_croupier = []
        self.joueur_actif = True
        self.croupier_actif = True

    def distribuer_carte(self, main):
        carte = random.choice(self.paquet)
        self.paquet.remove(carte)
        main.append(Carte(carte))

    def calculer_total(self, main):
        total = 0
        figures = ["V", "D", "R"]
        for carte in main:
            if carte.valeur in range(1, 11):
                total += carte.valeur
            elif carte.valeur in figures:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total

    def afficher_main_croupier(self):
        if len(self.main_croupier) == 2:
            return self.main_croupier[0]
        elif len(self.main_croupier) > 2:
            return self.main_croupier[0], self.main_croupier[1]

    def jouer(self):
        for _ in range(2):
            self.distribuer_carte(self.main_joueur)
            self.distribuer_carte(self.main_croupier)

        while self.joueur_actif or self.croupier_actif:
            print(f"Le croupier a {self.afficher_main_croupier()} et X")
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}")

            if self.joueur_actif:
                choix = input("1: Rester\n2: Tirer\n")

            if self.calculer_total(self.main_croupier) < 16:
                self.croupier_actif = False
            else:
                self.distribuer_carte(self.main_croupier)

            if choix == "1":
                self.joueur_actif = False
            elif choix == "2":
                self.distribuer_carte(self.main_joueur)

            if self.calculer_total(self.main_joueur) >= 21 or self.calculer_total(self.main_croupier) >= 21:
                break

        self.afficher_resultat()

    def afficher_resultat(self):
        print(f"\nLe croupier a {', '.join(str(carte) for carte in self.main_croupier)} pour un total de {self.calculer_total(self.main_croupier)}")
        if self.calculer_total(self.main_joueur) == 21:
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n")
            print("Blackjack ! Vous gagnez")
        elif self.calculer_total(self.main_croupier) == 21:
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n")
            print("Blackjack ! Le croupier gagne")
        elif self.calculer_total(self.main_joueur) > 21:
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n")
            print("Vous avez dépassé 21 ! Le croupier gagne")
        elif self.calculer_total(self.main_croupier) > 21:
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n") 
            print("Le croupier a dépassé 21 ! Vous gagnez")
        elif 21 - self.calculer_total(self.main_croupier) > 21 - self.calculer_total(self.main_joueur):
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n")
            print("Le croupier gagne")
        elif 21 - self.calculer_total(self.main_croupier) < 21 - self.calculer_total(self.main_joueur):
            print(f"Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n")
            print("Vous gagnez")
        else:
            print(f"Égalité ! Vous avez {', '.join(str(carte) for carte in self.main_joueur)} pour un total de {self.calculer_total(self.main_joueur)}\n")

# Création d'une instance de jeu et démarrage du jeu
jeu = Jeu()
jeu.jouer()
