from random import *
from tkinter import *
from Grille_2048 import *

couleurCase = {0:'white',2:'yellow2',4:'yellow3',8:'yellow4',16:'dark goldenrod',32:'goldenrod',64:'goldenrod3',128:'goldenrod2',256:'goldenrod1',512:'light goldenrod',1024:'gold2',2048:'gold'}


grille = ' '
x0,y0=20,20
taille = 90
nbCase = 6

def affichage(zone,message):
    """
    La fonction affichage permet d'afficher quel joueur doit jouer
    :param message: le message a afficher sur l'interface graphique
    :type message: str
    """
    zone.pack(side=TOP)
    zone.delete("0.0", END)
    zone.insert(END, message)

def affiche (grille):
    k=0
    for i in grille :
        for j in i :
            print (j,end=' ')
            k+=1
            if k == len(grille):
                print('\n')
                k=0
            

def appartient(x,g) :
    res = 0
    for i in g :
        if x in i :
            res += 1
    if res != 0 :
        return True
    else:
        return False

def gagnante(g):
    return appartient(2048,g)

def pleine (g) :
    return appartient (0,g)

def maximum (g):
    maxi = 0
    for i in g:
        for j in i:
            if j > maxi:
                maxi = j
    return maxi

def lescases (g,val):
    res=()
    for i in range (len (g)):
        for j in range (len(g)):
            if g[i] [j] == val :
                res += (i,j),
    print(res)
    return res

def vides(g):
    return lescases(g,0)
    
    
def ajouteAlea(g,val) :
    i = randint(0,len(g)-1)
    j = randint(0,len(g)-1)
    
    if g [i] [j] == 0:
        g[i] [j] = val

    else :
        return ajouteAlea(g,val)

def couleur(nb):
    return couleurCase[nb]

def CreeGrille(zone,grille):

    can.delete(ALL)
    
    for i in range(nbCase+1):
        can.create_line(x0+taille*i, y0,x0+taille*i,y0 + nbCase*taille)
        can.create_line(x0, y0+taille*i,x0+nbCase*taille ,y0+taille*i)
        
    for i in range(nbCase):
        for j in range(nbCase):
            x = grille[i][j]
            if x == 2048:
                decalage = (0.75)*taille;
                can.create_rectangle((j*taille)+30,(i*taille)+30,(j*taille)+taille+20,(i*taille)+c+20,fill=couleur(x),outline='')
                can.create_text((j*taille)+decalage,(i*taille)+decalage,text=str(x),font=("Ubuntu",13,"bold"),fill="gray20")
            elif x==0:
                decalage = (0.75)*taille
                can.create_rectangle((j*taille)+30,(i*taille)+30,(j*taille)+taille+20,(i*taille)+taille+20,fill=couleur(x),outline='')
                can.create_text((j*taille)+decalage,(i*taille)+decalage,text=str(x),font=("Ubuntu",12,"bold"),fill="gray26")
                
            else:
                decalage = (0.75)*taille;
                can.create_rectangle((j*taille)+25,(i*taille)+25,(j*taille)+taille+20,(i*taille)+taille+20,fill=couleur(x),outline='')
                can.create_text((j*taille)+decalage,(i*taille)+decalage,text=str(x),font=("Ubuntu",12,"bold"),fill="gray26")



def new() :
    global grille
    grille=creeGrille(nbCase,0)
    val= randint(1,2)
    if val == 1:
        val = 2
    else :
        val = 4
        
    ajouteAlea(grille,val)

    val= randint(1,2)
    if val == 1:
        val = 2
    else :
        val = 4
        
    ajouteAlea(grille,val)
    affiche (grille)
    CreeGrille(can,grille)

def quitter():
    fenetre.quit()
    fenetre.destroy()

def droite(event):
    global grille
    taille = len(grille)
    
    
    
    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if j-1 >=0 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i] [j-1]
                    grille[i] [j-1] = 0

    for i in range (taille) :
            for j in range (taille):
                if j-1 >=0 and grille[i] [j] == grille [i] [j-1] :
                    grille[i] [j] = grille[i] [j] * 2
                    grille [i] [j-1] =0

    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if j-1 >=0 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i] [j-1]
                    grille[i] [j-1] = 0
    
    Val_score = maximum(grille)
    affichage(texte,"Vous avez un score de : "+ str(Val_score))

    if gagnante(grille) == True :
        can.delete(ALL)
        can.create_text(300,300,text = "Vous avez Gagné(e), Bravo",font=("Ubuntu",30,"bold"),fill="gray26")
    else :
        val= randint(1,2)
        if val == 1:
            val = 2
        else :
            val = 4
            
        ajouteAlea(grille,val)
        
        CreeGrille(can,grille)
        
        if pleine(grille) == False :
            can.delete(ALL)
            affichage(texte,"Vous avez perdu, votre score est de : "+ str(Val_score))
    return grille

    


def gauche (event) :
    global grille
    taille = len(grille)
    
    
    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if j+1 <=taille-1 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i] [j+1]
                    grille[i] [j+1] = 0

    for i in range (taille) :
        for j in range (taille):
            if j+1 <=taille-1 and grille [i] [j] == grille [i] [j+1] :
                grille[i] [j] = grille[i] [j] * 2
                grille [i] [j+1] =0
                
    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if j+1 <=taille-1 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i] [j+1]
                    grille[i] [j+1] = 0
        
    Val_score = maximum(grille)
    affichage(texte,"Vous avez un score de : "+ str(Val_score))

    if gagnante(grille) == True :
        can.delete(ALL)
        can.create_text(300,300,text = "Vous avez Gagné(e), Bravo",font=("Ubuntu",30,"bold"),fill="gray26")
    else :
        val= randint(1,2)
        if val == 1:
            val = 2
        else :
            val = 4
            
        ajouteAlea(grille,val)
        
        CreeGrille(can,grille)
        
        if pleine(grille) == False :
            can.delete(ALL)
            affichage(texte,"Vous avez perdu, votre score est de : "+ str(Val_score))
    return grille


def haut (event) :
    global grille
    taille = len(grille)
    
    
    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if i+1 <= taille-1 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i+1] [j]
                    grille[i+1] [j] = 0

    for i in range (taille) :
            for j in range (taille):
                if i+1 <= taille-1 and grille [i] [j] == grille [i+1] [j] :
                    grille[i] [j] = grille[i] [j] * 2
                    grille [i+1] [j] =0

    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if i+1 <= taille-1 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i+1] [j]
                    grille[i+1] [j] = 0

    Val_score = maximum(grille)
    affichage(texte,"Vous avez un score de : "+ str(Val_score))

    if gagnante(grille) == True :
        can.delete(ALL)
        can.create_text(300,300,text = "Vous avez Gagné(e), Bravo",font=("Ubuntu",30,"bold"),fill="gray26")
    else :
        val= randint(1,2)
        if val == 1:
            val = 2
        else :
            val = 4
            
        ajouteAlea(grille,val)
        
        CreeGrille(can,grille)
        
        if pleine(grille) == False :
            can.delete(ALL)
            affichage(texte,"Vous avez perdu, votre score est de : "+ str(Val_score))
    return grille

def bas (event) :
    global grille
    taille = len(grille)
    
    
    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if i-1 >=0 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i-1] [j]
                    grille[i-1] [j] = 0

    for i in range (taille) :
            for j in range (taille):
                if i-1 >=0 and grille [i] [j] == grille [i-1] [j] :
                    grille[i] [j] = grille[i] [j] * 2
                    grille [i-1] [j] =0

    for k in range (taille):
        for i in range (taille):
            for j in range (taille):
                if i-1 >=0 and grille [i] [j] == 0:
                    grille[i] [j] = grille [i-1] [j]
                    grille[i-1] [j] = 0

    Val_score = maximum(grille)
    affichage(texte,"Vous avez un score de : "+ str(Val_score))

    if gagnante(grille) == True :
        can.delete(ALL)
        can.create_text(300,300,text = "Vous avez Gagné(e), Bravo",font=("Ubuntu",30,"bold"),fill="gray26")
    else :
        val= randint(1,2)
        if val == 1:
            val = 2
        else :
            val = 4
            
        ajouteAlea(grille,val)
        
        CreeGrille(can,grille)
        
        if pleine(grille) == False :
            can.delete(ALL)
            affichage(texte,"Vous avez perdu, votre score est de : "+ str(Val_score))
    return grille


fenetre=Tk()

jeu=Label(fenetre,text="AKIBA",font=("Ubuntu",20,"bold")).pack()


can=Canvas(fenetre,height=600,width=600,bg="white")
can.pack(side=LEFT)

Bdepart = Button(fenetre,text="Jouer",command=new,font=("Ubuntu",20,"bold"))
Bdepart.pack(side=TOP)



fenetre.bind("<Up>", haut)
fenetre.bind("<Left>", gauche)
fenetre.bind("<Down>", bas)
fenetre.bind("<Right>", droite)




texte = Text(fenetre, height=2, width=30 ,font=("Ubuntu",20,"bold"))
texte.pack(side = TOP)


Bquitter = Button(fenetre,text="quitter",command=quitter,font=("Ubuntu",20,"bold"))
Bquitter.pack(side = BOTTOM)

fenetre.mainloop()
