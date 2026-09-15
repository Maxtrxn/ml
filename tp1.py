import copy
import numpy as np
class Jeu_Hanoi:
    def __init__(self):
        self.pic = np.zeros([3,3],dtype=int)
        self.nombre_palet = np.zeros(3,dtype=int)
        pass
jeu = Jeu_Hanoi()
jeu.nombre_palet[0] = 3
jeu.pic[0, 0] = 3
jeu.pic[0, 1] = 2
jeu.pic[0, 2] = 1

Jeu_final = Jeu_Hanoi()
Jeu_final.nombre_palet[2] = 3
Jeu_final.pic[2, 0] = 3
Jeu_final.pic[2, 1] = 2
Jeu_final.pic[2, 2] = 1

def nombre_situation(jeu):
    code = ""
    for i in [2, 1, 0]:
        for j in [2, 1, 0]:
            if jeu.pic[i,j] != 0 :
                code += "1"
            else:
                code += "0"
    return int(code,2)

def pic_vide(indice_pic, jeu):
    return jeu.pic[indice_pic, 0] == 0 and jeu.pic[indice_pic, 1] == 0 and jeu.pic[indice_pic, 2] == 0
print(pic_vide(0, Jeu_final))

def regle_jeu(pic1, pic2, jeu):
    if pic1 == pic2:
        return False
    
    elif pic_vide(pic1, jeu):
        return False
    
    elif pic_vide(pic2, jeu):
        return True
    nbr_pic1 = jeu.nombre_palet[pic1]
    nbr_pic2 = jeu.nombre_palet[pic2]

    top_pic1 = jeu.pic[pic1, nbr_pic1 - 1]
    top_pic2 = jeu.pic[pic2, nbr_pic2 - 1]
    return top_pic1 < top_pic2

print(regle_jeu(1, 0, jeu))

def effectue_deplacement(pic1, pic2, jeu):
    if regle_jeu(pic1, pic2, jeu):
        nbr_pic1 = jeu.nombre_palet[pic1]
        nbr_pic2 = jeu.nombre_palet[pic2]
        
        top_pic1 = jeu.pic[pic1, nbr_pic1 - 1]

        jeu.pic[pic1, nbr_pic1 - 1] = 0
        jeu.pic[pic2, nbr_pic2] = top_pic1

        jeu.nombre_palet[pic1] -= 1
        jeu.nombre_palet[pic2] += 1

def situation_non_vue(pic1, pic2, jeu, situation_etudiee):
    simulation = copy.deepcopy(jeu) # necessite import copy et sert à faire une copie profonde de jeu pour ne pas avoir une reference de jeu
    effectue_deplacement(pic1, pic2, simulation)
    nb = nombre_situation(simulation)

    return nb not in situation_etudiee