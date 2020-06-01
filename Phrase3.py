from upemtk import *
from random import *
import time
import random
import copy
import sys
case_taille=50
information_bar=2*case_taille

def affiche_perdu():
    rectangle(0,haut_fenetre//3,long_fenetre,haut_fenetre*2//3,'tomato','tomato')
    texte(long_fenetre//2,haut_fenetre//2,"Perdu!","black","center")
    

def affiche_gagne():
    rectangle(0,haut_fenetre//3,long_fenetre,haut_fenetre*2//3,'darkorange','darkorange')
    texte(long_fenetre//2,haut_fenetre//2,"Gagné!","black","center")
    
def affiche_pause():
    rectangle(0,haut_fenetre//3,long_fenetre,haut_fenetre*2//3,'darkorange','darkorange')
    texte(long_fenetre//2,haut_fenetre//2,"Pause...","white","center")

def affiche_temps(temps_reste):
    texte(0,case_taille//2,str(temps_reste)+' s',"red")

def affiche_diament_need_et_gagne():
    texte(long_fenetre//3,case_taille//2,str(diamant_gagne)+'/'+str(diamant_need),"black")

def affiche_note_total():
    texte(long_fenetre*2//3,case_taille//2,diamant_gagne*note,'tomato')

def affiche_information() :
    rectangle(0,0,long_fenetre,information_bar,'white','white')

def affiche_plan(plan) : #affiche le plan selon les tailles de liste et attributs d'éléments.
    couleur=''
    for l in range(len(plan)) :
        for c in range(len(plan[l])) :
            if plan[l][c] == 'W' :
                couleur='saddlebrown'
            elif plan[l][c] == 'G' :
                couleur='sandybrown'
            elif plan[l][c] == 'B' :
                couleur='slategray'
                cercle(c*case_taille+case_taille/2,l*case_taille+case_taille/2+information_bar,case_taille/2-2,'black',couleur)
                continue
            elif plan[l][c] == 'D' :
                couleur='tomato'
                cercle(c*case_taille+case_taille/2,l*case_taille+case_taille/2+information_bar,case_taille/2-2,'black',couleur)
                continue
            elif plan[l][c] == '.' :
                couleur='white'
            elif plan[l][c] == 'R' :
                couleur='blueviolet'
            elif plan[l][c] == 'E' :
                couleur='olivedrab'
            elif plan[l][c] == 'F' :
                couleur='black'
            rectangle(c*case_taille,l*case_taille+information_bar,c*case_taille+case_taille,l*case_taille+case_taille+information_bar,'black',couleur)


def obtenir_position(plan,elem):  # Retourner la position de valeur elem
    """
    >>> plan=['W','W','W','W','R']
    >>> obtenir_position(plan,'R')
    [4, 0]
    """
    lst=[]
    for l in range(len(plan)):
        if elem  in plan[l]:
            lst.append(l)
            lst.append(plan[l].index(elem))
    return lst


def deplacer(plan,direction):
    global temps_demarrer
    global plan_original
    global diamant_gagne

    x,y=obtenir_position(plan,'R')
    # Selon la structure de liste, 'x' est le coordonnée vertical, 'y' est le coordonnée horizontal.


    if direction=='haut':
        if plan[x-1][y] in 'G.DE':
            plan[x][y]='.'
            plan[x-1][y]='R'

    if direction=='bas':
        if plan[x+1][y] in 'G.DE':
            plan[x][y]='.'
            plan[x+1][y]='R'

    if direction=='droite':
        if plan[x][y+1] in 'G.DE':
            plan[x][y]='.'
            plan[x][y+1]='R'
        elif plan[x][y+1]=='B': # Pour pousser le rocher.
            if plan[x][y+2]=='.':
                plan[x][y+2]='B'
                plan[x][y+1]='R'
                plan[x][y]='.'
    if direction=='gauche':
        if plan[x][y-1] in 'G.DE':
            plan[x][y]='.'
            plan[x][y-1]='R'
        elif plan[x][y-1]=='B': # Pour pousser le rocher.
            if plan[x][y-2]=='.':
                plan[x][y-2]='B'
                plan[x][y-1]='R'
                plan[x][y]='.'

    return plan

def count_diament_gagne(plan):
    count=0
    for i in range(len(plan)):
        for j in range(len(plan[i])) :
            if plan[i][j]=='D':
                count+=1
    return diamant_total-count
def ouvert_porte(n,plan):
    if n == diamant_need:
        plan[out[0]][out[1]] = 'E'
        return plan
    return plan


def tomber_rocher_et_diamond_et_quitter_ce_monde(plan):
    '''
    if plan[ford[0]-1][ford[1]] in 'BD':
        plan[ford[0]][ford[1]]=plan[ford[0]-1][ford[1]]
        plan[ford[0]-1][ford[1]]='.'
    '''
    for i in range(len(plan[0])) : # Parcourir les trois colonne qui entournent Rockford.
        for j in range(len(plan)-2,0,-1): # Parcourir tout les lignes.
            if plan[j][i] in 'BD' and plan[j+1][i] == '.' : # Examiner l'élément au-dessous de rocher.
                plan[j+1][i]=plan[j][i]
                plan[j][i]='.' 
                
                if plan[j+2][i]=='R':
                    plan[j+2][i]=plan[j+1][i]
                    plan[j+1][i]='.'
                
            if plan[j][i] in 'BD' and plan[j-1][i] in 'BD' and plan[j][i+1]=='.' and plan[j-1][i+1]=='.': # droite
                plan[j][i+1]=plan[j-1][i]
                plan[j-1][i]='.'
                
                if plan[j+1][i+1]=='R' :
                    plan[j+1][i+1]=plan[j][i+1]
                    plan[j][i+1]='.'
                

            if plan[j][i]in 'BD' and plan[j-1][i]in 'BD' and plan[j][i-1]=='.' and plan[j-1][i-1]=='.': # gauche
                plan[j][i-1]=plan[j-1][i]
                plan[j-1][i]='.'
                
                if plan[j+1][i-1]=='R':
                    plan[j+1][i-1]=plan[j][i-1]
                    plan[j][i-1]='.'
                
    return plan

def debug():
    direction=['haut','bas','droite','gauche']
    nd=randint(0,3) # Choisir la direction aléatoire.
    return direction[nd]

def ecoulement() :
    return  temps_total-int(time.time()-temps_demarrer)

def ouvert_file(entre):
    with open(entre) as f:
        s = f.readline().replace("d","s").replace("n","s")
        lst = s.split("s")    #separer le temps et nb_diamant
        temps_total = int(lst[0])
        diamant_need = int(lst[1]) 
        note = int(lst[2])
        meilleur_score = int(lst[3])
        
        lst_p = [ line[:-1] for line in f.readlines()]
        plan = []
        for i in range(len(lst_p)):
            plan.append([])
            for ele in lst_p[i]:
                plan[i].append(ele)
        
    return plan,temps_total,diamant_need,note,meilleur_score

def le_meilleur_score(sortie):
    global meilleur_score
    ms = diamant_gagne*note
    if 'R'  in set(case for ligne in plan for case in ligne) :
        ms+=temps_reste
    if ms > meilleur_score : 
        meilleur_score = ms 
    texte(long_fenetre//4+case_taille,haut_fenetre//2+case_taille,"votre score:"+str(ms),"white","center","",20)
    texte(long_fenetre//4*2+3*case_taille,haut_fenetre//2+case_taille,"le meilleur score:"+str(meilleur_score),"white","center","",20)
    with open(sortie,'r+') as s:
        lines  = s.readlines()      #faire une copie de text
        #print(lines)
        s.seek(0,0)
        for i in range(len(lines)):
            if i==0:
                s.write('{}s {}d {}n {}s'.format(temps_total,diamant_need,note,meilleur_score)+'\n')
            else:
                s.write(lines[i])
def niveau_choix():
    r = 1
    f = 1
    niveau1 = [8,14,5,7,6,0]
    niveau2 = [8,17,7,16,9,3]
    niveau3 = [8,20,9,20,8,8]

    while True:
        ev = donne_evenement()
        type_ev = type_evenement(ev)
        if type_ev == "ClicDroit" or type_ev == "ClicGauche":
            x = clic_x(ev)
            y = clic_y(ev)
            if x >= l and x <= l*2 and y >= h and y<= h*3:
                niveau = 1
                break
            elif x >= l and x <= l*2 and y >= h*4 and y<= h*6:
                niveau = 2
                break
            elif x >= l and x <= l*2 and y >= h*7 and y<= h*9:
                niveau = 3
                break
        mise_a_jour()

    niveaus_dico = {1:niveau1,2:niveau2,3:niveau3}

    m,n,d,b,v,w = niveaus_dico[niveau]
    while True:
        M = [] 
        for i in range(m):
            M.append([])
            for j in range(n):
                M[i].append(None) 

        for i in range(m):
            M[i][0] = 'W'
            M[i][n-1] = 'W'

        for j in range(n):
            M[0][j] = 'W'
            M[m-1][j] = 'W'
        c = 0
        while c < r:
            x = random.randint(1,m-2)
            y = random.randint(1,n-2)
            if M[x][y] == None:
                M[x][y] = 'R'
                c += 1
        c = 0
        while c < f:
            x = random.randint(1,m-2)
            y = random.randint(1,n-2)
            if M[x][y] == None:
                M[x][y] = 'F'
                c += 1
        c = 0
        while c < d:
            x = random.randint(1,m-2)
            y = random.randint(1,n-2)
            if M[x][y] == None:
                M[x][y] = 'D'
                c += 1
        c = 0
        while c < b:
            x = random.randint(1,m-2)
            y = random.randint(1,n-2)
            if M[x][y] == None:
                M[x][y] = 'B'
                c += 1
        c = 0
        while c < v:
            x = random.randint(1,m-2)
            y = random.randint(1,n-2)
            if M[x][y] == None:
                M[x][y] = '.'
                c += 1
        c = 0
        while c < w:
            x = random.randint(1,m-2)
            y = random.randint(1,n-2)
            if M[x][y] == None:
                M[x][y] = 'W'
                c += 1

        for i in range(1,m-1):
            for j in range(1,n-1):
                if M[i][j] == None:
                    M[i][j] = 'G'
        x,y = obtenir_position(M,"R")
        for voisin in [M[x-1][y],M[x][y-1],M[x+1][y],M[x][y+1]] :
            if voisin not in "WBF" :
                return M,niveau


def affiche_niveau():
	
    rectangle(l,h,l*2,h*3,'gray','rosybrown',5)
    texte(l*1.5,h*2,"NIVEAU1","white","center","Purisa",19)

    rectangle(l,h*4,l*2,h*6,'gray','rosybrown',5)
    texte(l*1.5,h*5,"NIVEAU2","white","center","Purisa",19)

    rectangle(l,h*7,l*2,h*9,'gray','rosybrown',5)
    texte(l*1.5,h*8,"NIVEAU3","white","center","Purisa",19)


if __name__ == '__main__':
    liste_argv = sys.argv
    length = len(liste_argv)
    niveau=["plan1.txt","plan2.txt","plan3.txt"]
    if length == 1:
        haut_fenetre = 400  # tailles de la fenêtre
        long_fenetre = 400  # tailles de la fenêtre
        l = long_fenetre//3 # positions des trois niveaus
        h = haut_fenetre//10# positions des trois niveaus
        cree_fenetre(long_fenetre,haut_fenetre)
        affiche_niveau()
        plan_original,num_niveau=niveau_choix() # initialisation de plan aléatoire
        cercle(l//2,h*(3*(num_niveau-1)+2),h//2,'lightslategray','lightslategray') # niveau choyant
        mise_a_jour()
        time.sleep(1)
        ferme_fenetre()
        # note: score de chaque diamant 
        _,temps_total,diamant_need,note,meilleur_score=ouvert_file(niveau[num_niveau-1]) 
    elif length == 2:
        plan_original,temps_total,diamant_need,note,meilleur_score=ouvert_file(liste_argv[1]) 
        num_niveau=list(a for a,b in list(enumerate(niveau, start=1)) if b==liste_argv[1])[0]

    plan=copy.deepcopy(plan_original)
    haut_fenetre=len(plan)*case_taille+information_bar # taille de fenêtre par rapport au plan 
    long_fenetre=len(plan[0])*case_taille
    cree_fenetre(long_fenetre,haut_fenetre)
    #direction='droite'
    out=obtenir_position(plan,'F')     # Obtenir la coordonnée de sortie.
    ford=obtenir_position(plan,'R')
    switch=False # switch pour debug
    diamant_total=len([case for ligne in plan_original for case in ligne if case=='D'])
    diamant_gagne=0
    temps_reste=temps_total # initialisation du temps reste
    temps_demarrer=time.time() # temps courant
    
    plan=tomber_rocher_et_diamond_et_quitter_ce_monde(plan) 
    affiche_plan(plan)
    #diamant_gagne=count_diament_gagne(plan)
    temp=1
    intervalle=3000
    while True:
        #ford=obtenir_position(plan,'R')   # Obtenir la coordonnée de Rockford.
        #if not switch:
        ev=donne_evenement()
        type_ev=type_evenement(ev)

        if type_ev=="Touche" and touche(ev)=="d":
            switch = not switch
            if intervalle==3000:
                intervalle=5
            else :
                intervalle=3000
        if switch:
            type_ev="Touche"
        if type_ev=="Touche":
            if not switch:
                t=touche(ev)
                if t=="Right":
                    direction='droite'
                elif t=="Left":
                    direction='gauche'
                elif t=="Up":
                    direction='haut'
                elif t=="Down":
                    direction='bas'
                elif t=="r":          # Pour renouveler
                    plan=copy.deepcopy(plan_original)
                    temps_demarrer=time.time()
                    diamant_gagne=0
                elif t=="d":          # pour debug
                    direction=' '
                elif t=="p":  # pour faire une pause
                    affiche_pause()
                    attente_touche()
            else :
                #if  temp1 % 200 == 0:
                #if random.randint(1,20)==1:
                if temp%20 == 0 :
                    direction=debug()
                else :
                    direction=" "

            efface_tout()
            plan=deplacer(plan,direction)
            ford=obtenir_position(plan,'R')   # Obtenir la coordonnée de Rockford.
            if ford==out :
                affiche_plan(plan)
                affiche_information()   
                affiche_diament_need_et_gagne()
                affiche_note_total() # mise à jour du score total 
                affiche_temps(temps_reste)
                affiche_gagne()        #affiche 'GAGNE!' si il atteint la sortie.
                le_meilleur_score(niveau[num_niveau-1])
                mise_a_jour()
                attente_touche()
                break
            diamant_gagne=count_diament_gagne(plan) 
            plan=ouvert_porte(diamant_gagne,plan)
            ford=obtenir_position(plan,'R')   # Obtenir la coordonnée de Rockford.
            #direction=None
            affiche_plan(plan)
            affiche_information()   
            affiche_diament_need_et_gagne()
            affiche_note_total()
            temps_reste=ecoulement()
            affiche_temps(temps_reste)

            if not switch:
                temp=1 # renouveler le temps pour ralentir l'éboulement
        if  temp % intervalle == 0: # pour ralentir l'éboulement...
            plan=tomber_rocher_et_diamond_et_quitter_ce_monde(plan)
            if 'R' not in set(case for ligne in plan for case in ligne) :
                affiche_plan(plan)
                affiche_perdu()
                le_meilleur_score(niveau[num_niveau-1])
                break
            affiche_plan(plan)
            temps_reste=ecoulement() # Le temps qu'il reste.
            affiche_information()   
            affiche_diament_need_et_gagne()
            affiche_note_total() # mise à jour du score total 
            if temps_reste==0 :
                affiche_perdu()
                le_meilleur_score(niveau[num_niveau-1]) # lire le meilleur score à partir de fichier
                break
            affiche_temps(temps_reste) # affiche le temps qu'il reste.
        temp+=1
        mise_a_jour()
    mise_a_jour()
    time.sleep(1)
    attente_touche()
    ferme_fenetre()
