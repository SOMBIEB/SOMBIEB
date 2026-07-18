# ============================================================
#  Première fonction en Python — niveau 0
#  Analogie : une FONCTION = une RECETTE de cuisine
# ============================================================
#
#  Une recette a :
#    1) un NOM          →  def dire_bonjour
#    2) des INGRÉDIENTS →  les paramètres entre parenthèses
#    3) des ÉTAPES      →  le code indenté (décalé)
#    4) un PLAT FINI    →  return (ce qu'on renvoie)
#
#  IMPORTANT :
#  - Écrire la recette ≠ cuisiner
#  - Pour cuisiner, il faut APPELER la fonction : dire_bonjour()
# ============================================================


# ------------------------------------------------------------
# ÉTAPE 1 — Ta première fonction (sans ingrédient)
# ------------------------------------------------------------
# "def" veut dire : "je DÉFINIS une nouvelle recette"

def dire_bonjour():
    print("Bonjour !")


# On APPELE la fonction (on lance la recette) :
print("--- Étape 1 ---")
dire_bonjour()


# ------------------------------------------------------------
# ÉTAPE 2 — Une fonction avec un INGRÉDIENT (paramètre)
# ------------------------------------------------------------
# "prenom" est une case vide : on la remplit à l'appel

def saluer(prenom):
    print("Bonjour", prenom, "!")


print("--- Étape 2 ---")
saluer("Marie")
saluer("Alex")


# ------------------------------------------------------------
# ÉTAPE 3 — Une fonction qui RENVOIE un résultat (return)
# ------------------------------------------------------------
# print = affiche à l'écran
# return = donne le résultat à Python pour le réutiliser

def additionner(a, b):
    resultat = a + b
    return resultat


print("--- Étape 3 ---")
somme = additionner(3, 5)
print("3 + 5 =", somme)
print("10 + 2 =", additionner(10, 2))


# ------------------------------------------------------------
# ÉTAPE 4 — Mini-projet du jour : calculer un âge
# ------------------------------------------------------------

def calculer_age(annee_naissance, annee_actuelle):
    age = annee_actuelle - annee_naissance
    return age


print("--- Étape 4 ---")
mon_age = calculer_age(2000, 2026)
print("Tu as", mon_age, "ans.")


# ------------------------------------------------------------
# 🏋️ EXERCICE — À TOI DE JOUER
# ------------------------------------------------------------
# 1) Crée une fonction appelée "multiplier" qui prend 2 nombres
# 2) Elle doit RENVOYER (return) le produit des 2 nombres
# 3) Appelle-la avec 4 et 7, puis affiche le résultat
#
#  Indice : inspire-toi de "additionner" juste au-dessus.
#  Décommente (enlève les #) les lignes ci-dessous et complète.

# def multiplier(a, b):
#     ...   # remplace les ... par ton code
#
# print("--- Exercice ---")
# print(multiplier(4, 7))   # doit afficher 28


# ------------------------------------------------------------
# ✅ CORRECTION (regarde seulement après avoir essayé)
# ------------------------------------------------------------
# def multiplier(a, b):
#     return a * b
#
# print("--- Exercice ---")
# print(multiplier(4, 7))
