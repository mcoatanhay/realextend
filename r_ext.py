#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: realextend.py
# Auteur: Marc COATANHAY

"""
    Module python pour effectuer des calculs réels étendus.

"""

# Import des modules
try:
    import mes_modules_path
except:
    pass

import rationnels.ratio as ratio

# Définitions constantes et variables globales

# Définitions fonctions et classes
class RealExt():
    """Classe permettant d'effectuer des opérations sur réels étendus."""
    def __init__(self,type="reel",signe=1,mantisse=1,exposant=1):
        """Initialise un élément de class RealExt."""
        try:
            self.type = type
            self.signe = int(signe)
            self.mantisse = abs(int(mantisse))
            self.exposant = int(exposant)
        except:
            self.type = "indeterminé"
            self.signe = 1
            self.mantisse = 1
            self.exposant = 1

    def __repr__(self):
        """Affichage d'un terme Incert."""
        if(self.signe == -1):
            chaine = '-'
        else:
            chaine = '+'
        if(self.type == 'reel'):
            chaine += str(self.mantisse)
            chaine += "E"
            chaine += str(self.exposant)

        return chaine



print("* Module : reels étendus /ok")