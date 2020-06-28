# Boulder-Dash
les extensions qui ont été implémentées:
Extension 1.a 
Rajouter la gestion de la vitesse de déplacement (c’est-à-dire faire en sorte
que Rockford puisse échapper à un éboulement s’il se déplace assez vite).

Extension 2.a 
Rajouter un menu de sélection des niveaux et/ou du type de niveau (aléatoire
ou fichier). On doit néanmoins toujours avoir une version du jeu qui peut lire un fichier de
niveau en argument en ligne de commande et le lancer directement avec ce niveau.


L'organisation: 

1. Obtenir les arguments à partir de la ligne command
2. Si l'utilisateur choisit un plan aléatoire:
	2.1 Créer une fenètre
	2.2 Afficher les niveaux qui pouvez être choisi
	2.3 Obtenir le niveau qui est choisi par l'utilisateur
	2.4 Initialiser un plan aléatoire
	2.5 Afficher un point qui dirige a le niveau choisi
	2.6 Fermer la fenètre
	2.7 Obtenir le plan orginal,temps total,le nonbre de diamant nécessaire,le merilleur score à partir le fichier	
3.Si l'utilisatuer choisit un plan dans le fichier:
	3.1 Initialiser un plan à partir du fichier choisi
	3.2 Obtenir le plan orginal,temps total,le nonbre de diamant nécessaire,le merilleur score à partir le fichier

4. faire une copie profonde de plan orginal
5. Créer une fenètre
6. Obtenir la position de la sortie
7. Créer un interrupteur qui manipule le début et la fin de DEBUG (le interrupteur est éteint par defaut)
8. Compter les nombre total de diamant dans le plan orginal
9. Initialiser le nombre de diamant qui sont gagné par l'utilisateur
10. Initialiser le temps reste qui égale à temps total
11. Mémoriser le temps courant
12. Tomber les rochers
13. Afficher le plan
14. Créer un compteur(la valeur est 1 par defaut)
15. Créer un intervalle 


16 While True:
	16.1 Obtenir l'événement associé à la fenêtre.
	16.2 Si le type d'événement est "Touche" et l'événement est "d":
		16.2.2 Démarrer le interrupteur
		16.2.3 Si l'intervalle égale intervalle orginal:
			intervalle égale 5
		16.2.4 Sinon:
			intervalle égale intervalle orginal
	16.3 Si le type d'événement est "Touche":
	16.4 Déplacher ROCKFORD par rapport à l'instruction
16.Si ROCKFORD sortie :
	Affiche "Gagné",le score courant et le meilleur socre
	Terminer le jeu
17. Si ROCKFORD est mort:
	Affiche "Perdu", le score courant
	Terminer le jeu 
	


Le choix technique:
Une liste à deux dimensions pour conserver le plan.

Les problèmes :
1.On va afficher le même plan même si Rockford ne bouge pas.
2.Le programme change la liste original même si on a utilisé la fonction list(). La fonction reset() ne marche pas.
jlhlhll
