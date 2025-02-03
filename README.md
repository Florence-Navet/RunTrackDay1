# RunTrackDay1  

# Jour 1 Les Classes

+ **Job1**
Créez une classe Opération avec un constructeur (méthode qui sera appelée lors de l'instance de la classe)  
- Ajouter des attributs `nombre1` et `nombre2` initialisés avec des valeurs par défaut instanciés votre première classe et imprimez l'objet en console.  
  
+ **Job2**  
A l'aide de la classe _Operation_ crée au-dessus, imprimez en console la valeur des attibuts `nombre1` et `nombre2`.  
  
+ **Job3**  
Modifiez votre classe Operation afin d’y ajouter la méthode `addition()`. Cette
méthode additionne `nombre1` et `nombre2` et affiche en console le résultat.  
  
+ **Job4**  
Créez une classe _Personne_ avec les attributs _nom_ et _prenom_. Ajoutez une
méthode _SePresenter_ qui retourne le nom et le prénom de la personne.
Ajoutez aussi un constructeur prenant en paramètres de quoi donner des
valeurs initiales aux attributs _nom_ et _prenom_. Instanciez plusieurs personnes
avec les valeurs de construction de votre choix et faites appel à la méthode
_SePresenter_ afin de vérifier que tout fonctionne correctement.  
  
+ **Joo5**  
Créez une classe nommée _Point_ avec les attributs x et y correspondant aux
coordonnées horizontales et verticales du point. Les deux attributs doivent
être initialisés dans le constructeur.  
  
La classe _Point_ doit posséder les méthodes suivantes :  
➔ _afficherLesPoints_ qui affiche les coordonnées des points.  
➔ _afficherX_ et _afficherY_ qui affiche respectivement _x_ et _y_.  
➔ _changerX_ et _changerY_ qui change la valeur des attributs _x_ et _y_.  
  
+ **Job6**
Créez une classe _Animal_ avec un attribut age initialisé à zéro et prenom
initialisé vide dans son constructeur.
Instanciez un objet Animal et affichez en console l’attribut âge. Créez une
méthode _vieillir_ qui ajoute 1 à l'âge de l’animal. Faites _vieillir_ votre animal et
affichez son âge mis à jour en console.  
Créez une méthode _nommer_ qui prend en paramètre le nom de l’animal.
Nommez votre animal et affichez en console son nom.  
  
+ **Job7**  
Créez une classe _Personnage_ représentant un personnage de jeu. Le plateau
de jeu est représenté par une matrice. Le joueur est défini par ses attributs x
et y, représentant les index du tableau.  
Créez le _constructeur_ de cette classe en initialisant la position (x et y).
Créez les méthodes : _gauche_, _droite_, _bas_ et _haut_ permettant respectivement
de faire avancer à gauche et à droite, en haut ou en bas.  
Implémentez une méthode `_position_`renvoyant les coordonnées sous forme
d’un tuple.  
  
+ **Job8**
Créez la classe “Cercle” recevant en argument son rayon, également initialisé
dans le constructeur.  
Ajoutez les méthodes suivantes :
- changerRayon qui permet de modifier le rayon.  
- afficherInfos qui permet d’afficher toutes les informations du cercle.  
- circonférence qui permet de retourner la circonférence.  
- aire qui permet de retourner l’aire du cercle.
- diametre qui permet de retourner le diamètre du cercle.  
  
Créez deux cercles avec comme rayon 4 et 7. Pour chaque cercle, affichez ses
informations, affichez sa circonférence, son diamètre et son aire.  
  
+ **Job9**  
Créez la classe _Produit_ avec des attributs _nom_, _prixHT_, _TVA_. Implémentez la
méthode _CalculerPrixTTC_ qui retourne le prix produit avec la TVA. Ajoutez la
méthode _afficher_ qui liste l’ensemble des informations du produit.
Créez _plusieurs produits_ et calculez leurs TVA.  
Ajoutez des méthodes permettant de modifier le nom du produit et son prix.
Ainsi que des méthodes permettant de retourner chaque information du
produit.  
Modifiez le nom et le prix de chaque produit et affichez en console le nouveau
prix des produits.  
La fonction print() ne doit pas être utilisée dans la classe Produit.
Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices.  
