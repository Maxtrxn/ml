import copy
import numpy as np
class Jeu_Hanoi:
    def __init__(self, nb_pics=3, nb_palets=3):
        self.nb_pics = nb_pics
        self.nb_palets = nb_palets
        self.pic = np.zeros([nb_pics,nb_pics],dtype=int)
        self.nombre_palet = np.zeros(nb_palets,dtype=int)
        pass

    def __str__(self):
        txt = ""

        for i in range(self.nb_pics):
            txt += f"Pic {i}: {self.pic[i]} nb_palet: {self.nombre_palet[i]}\n"

        return txt
        """ # version moins modulaire utilisable qu'avec 3 pic 3 palets
        return(
            f"Pic 0: {self.pic[0]} & nb_palet: {self.nombre_palet[0]}\n"
            f"Pic 1: {self.pic[1]} & nb_palet: {self.nombre_palet[1]}\n"
            f"Pic 2: {self.pic[2]} & nb_palet: {self.nombre_palet[2]}\n"

        )
        """

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
        # on teste d'abord le disque 3 puis le 2 et le 1
        # comme on veut le disque 3 a gauche et le disque 1 a droite
        # dans l'ecriture du triplet pour un pic
        for j in [3,2,1]:
            # on regarde si le disque est sur le pic, si oui on ecris 1 sinon 0
            if j in jeu.pic[i] :
                code += "1"
            else:
                code += "0"
    return int(code,2)


def pic_vide(indice_pic, jeu):
    return jeu.pic[indice_pic, 0] == 0 and jeu.pic[indice_pic, 1] == 0 and jeu.pic[indice_pic, 2] == 0


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


def moteur(jeu):
    nb_coups = 0
    code_final = nombre_situation(Jeu_final)
    situation_etudiee = [nombre_situation(jeu)]

    while nombre_situation(jeu) != code_final:
         #premiere optimisation : passe de 26 a 9 coups
        if regle_jeu(0, 2, jeu) and situation_non_vue(0, 2, jeu, situation_etudiee):
            effectue_deplacement(0, 2, jeu)
            situation_etudiee.append(nombre_situation(jeu))

        elif regle_jeu(0, 1, jeu) and situation_non_vue(0, 1, jeu, situation_etudiee):
            effectue_deplacement(0, 1, jeu)
            situation_etudiee.append(nombre_situation(jeu))

        elif regle_jeu(1, 2, jeu) and situation_non_vue(1, 2, jeu, situation_etudiee):
            effectue_deplacement(1, 2, jeu)
            situation_etudiee.append(nombre_situation(jeu))

        elif regle_jeu(2, 1, jeu) and situation_non_vue(2, 1, jeu, situation_etudiee):
            effectue_deplacement(2, 1, jeu)
            situation_etudiee.append(nombre_situation(jeu))

        elif regle_jeu(1, 0, jeu) and situation_non_vue(1, 0, jeu, situation_etudiee):
            effectue_deplacement(1, 0, jeu)
            situation_etudiee.append(nombre_situation(jeu))

        else:
            return "ERROR: pas de coups possible"

        nb_coups += 1
        print(f"Coup: {nb_coups}")
        print(jeu)
    return nb_coups

print(jeu)
print(f"nb_coups: {moteur(jeu)}")
