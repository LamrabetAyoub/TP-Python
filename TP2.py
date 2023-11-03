# # Exercice1
n = input("donner un nombre :")
int(n)
m = n + n * 11 + n * 111 + n * 1111
print("", n, "+", n, n, "+", n, n, n, "+", n, n, n, n, "=", m)
# Eercice 2
n = int(input("donner la taille de triangle :"))
c = 0
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print(" ")
for i in range(0, n):
    c += 1
    for j in range(0, i + 1):
        print(f"{c}", end="")
    print(" ")
# exercice 3:
import random

n = random.randint(1, 100)
nbessai = 7
print(
    "***** On va jouer a un petit jeu, je vais génerer un nombre antre 1 et 100 et tu vas le devinez en 7 essais ******")
for i in range(0, nbessai):
    nb = int(input("Donner un nombre entre 1 et 100 :"))
    if n == nb:
        print(f"Bravo {nb} est le nombre que j'ai choisit vous l'avez deviné en {i} essais")
        break
    elif nb < n:
        print("Oups, entrez un nombre plus grand")
    elif nb > n:
        print("Oups, entrez un nombre plus petit")
    elif nb < n or nb > n:
        print("oups, vous avez saisi un nombre en dehors de l intervalle")

if n != nb:
    print("Désolé vous avez utilisé tous vos essais")
# # exercice4
L = [1, -30, -2, 500, 4, 2, 100]
Lp = []
Ln = []

for i in L:
    if i > 0:
        Lp.append(i)
    elif i < 0:
        Ln.append(i)
L = Lp + Ln
print(L)
# Exercice5:
L = [1, 2, 3, 4, 5, 6, 7, 8]
v = int(input("Donner une valeur a inserer :"))
i = 0
while i < len(L) and L[i] < v:
    i += 1
L.insert(i, v)
print(L)
# exercice6:
L = [1, 2, 3, 5, 2, 1, 3, 5, 9, 78, 1, 78, 88, 2, 1]
Nl = []
n = int(input("Donner le nombre :"))
for i in L:
    if i != n:
        Nl.append(i)
print(Nl)
# exercice7:
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 2, 8, 8]
Nl = []
for i in L:
    if i not in Nl:
        Nl.append(i)
print(Nl)
# exercice 8:
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 2, 8, 8]
n = int(input("Donner le nombre a chercher :"))
L_o_c = []
for i in range(0, len(L)):
    if L[i] == n:
        L_o_c.append(i)

if len(L_o_c) != 0:
    print(f"les occurances de nombre inserer {n} sont {len(L_o_c)} ses posistions sont {L_o_c} ")
else:
    print("le nombre n'a pas d'occurance.")
# exercice 9:
d = input("Direction e: euro vers mad /m:mad vers euro : ").lower()
v = []
while 1:
    x = float(input("Valeur (négatif pour arrêter) : "))
    if x < 0:
        break
    v.append(x)
c, r = [], 'eur'
if d == 'm':
    r = 'mad'
    c = [x * 0.092 for x in v]
elif d == 'e':
    c = [x * 10.86 for x in v]
for i in range(len(v)):
    print(f"{v[i]} {r} équivaut à {c[i]:.2f} {['mad', 'eur'][r == 'mad']}")
# exercice 10:
L1 = [1, 3, 6, 78, 35, 88, 55]
L2 = [12, 24, 35, 24, 88, 120, 155]
L3 = []
for i in L1:
    if i in L2:
        L3.append(i)
print(L3)
# exercice 11
L1 = [8, 24, 48, 2, 16]
L2 = []
for i in range(len(L1) - 1, -1, -1):
    L2.append(L1[i])
print(L2)