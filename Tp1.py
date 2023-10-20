#Exercice1
a=int(input("Saisir une valeur "))
b=a+1
print(b)
# Exercice2
age=int(input("Donnez votre Age :"))
Taille=float(input("donnez votre taille en m :"))
print("Vous avez",age,"ans et vous mesurez",Taille,"m")
# Exercice3
Distance=float(input("Donnez la disatnce en Kilomètre: "))*1000
Temps=float(input("Donnez le temps en minute: "))*60
print(Distance,"\n",Temps)
print ("La vitess est", Distance/Temps, "m/s")
# Exercice 4
sec=int(input("Donnez le nombre de scondes : "))
h=sec//3600
sec%=3600
m=sec//60
sec%=60
print(sec,"secondes=",h,"H",m,"min",sec,"s")
# Exercice 5
N=int(input("Donner votre nombre :"))
if N%2==0 :
    print("Ce nombre est pair")
else:
    if (N%2!=0) and (N%3==0):
         print("Ce nombre est impair, mais multiple de 3")
    else :
         print("Ce nombre ni pair, ni multiple de 3")
# Exercice 6
a=int(input("Donner un nombre :"))
b=int(input("Donner un nombre :"))
if a>0 and b>0 or a<0 and b<0:
    print("Le prouit est positif")
else :
    print("Le produit est negatif")
# Exercice 7
a=int(input("Donnez votre 1er nombre: "))
b=int(input("Donnez votre 2eme nombre: "))
ope=str(input("Donner votre opertaeur (+,-,*,/) : "))
if ope=='+':
        print(a,ope,b,"=",a+b)
elif ope=='-':
        print(a,ope,b,"=",a-b)
elif ope=='*':
        print(a,ope,b,"=",a*b)
elif ope=='/':
    if b!=0:
            print(a,ope,b,"=",a/b)
    else:
         print ("Erreur:Division par zero")
else:
        print("Error:Opération no valide")
# Exercice 8
Sm=0
Sc=0
i=0
for i in range(0,4):
    T=list(range(0,4))
    print("Donner La note ",i+1)
    T[i]=float(input())
    c=float(input("Donner le coeficient :"))
    Sm+=T[i]*c
    Sc+=c
Note=float(Sm/Sc)
if Note>=10:
    print("La moyenne de ces 4 notes est ",Note,"semsetre validé")
elif 7<Note<10:
    print("La moyenne de ces 4 notes est ",Note,"semsetre rattrapage")
else:
    print("La moyenne de ces 4 notes est ",Note,"semsetre est non Validé")
# Exercice 9
article=[]
i=0
while(i<2):
    print("Donner le nom de larticle ",i+1)
    na=input()
    print("Donner la quantité de l article ",i+1)
    qt=int(input())
    print("Donner le prix unitaire de l article",i+1)
    p=float(input())
    pht=qt*p
    pttc=pht + pht*0.2
    arti=[na,qt,p,pht,pttc]
    article.append(arti)
    i+=1
for i,ar in enumerate(article):
   print(f"Totale pour l'article {ar[0]}:{ar[3]} dh (ht)")
total=0
for ar in article:
    total+=ar[4]
print(f"le total de votre facture est: {total}")
# Execice 10
user=input("Donnez Votre Username :")
passw=input("Donnez Votre Mots de passe :")
if user=="admin" and passw=="admin":
    print ("Bienvenue")
else:
    print ("login et le mot de passe saisie sont incorrecte")
# Exercice 11
poids = float(input("Entrez votre poids en kg : "))
taille = float(input("Entrez votre taille en mètres : "))

imc = poids / (taille ** 2)

if imc > 40:
    interpretation = "Obésité morbide ou massive"
elif 35 <= imc < 40:
    interpretation = "Obésité sévère"
elif 30 <= imc < 35:
    interpretation = "Obésité modérée"
elif 25 <= imc < 30:
    interpretation = "Surpoids"
elif 18.5 <= imc < 25:
    interpretation = "Corpulence normale"
elif 16.5 <= imc < 18.5:
    interpretation = "Maigreur"
else:
    interpretation = "Famine"

print(f"Votre IMC est de {imc:.2f}, ce qui correspond à : {interpretation}")
# Exercice 12
grade = input("Entrez le grade de l'employé (A, B, C, D, ou E) : ")
nombre_heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))

tarif_horaire = 0
prime = 0

if grade == 'A':
    tarif_horaire = 200
    prime = (nombre_heures_travaillees // 20) * 1000
elif grade == 'B':
    tarif_horaire = 150
    prime = (nombre_heures_travaillees // 20) * 800
elif grade == 'C':
    tarif_horaire = 120
    prime = (nombre_heures_travaillees // 15) * 500
elif grade == 'D':
    tarif_horaire = 100
    prime = (nombre_heures_travaillees // 15) * 350
elif grade == 'E':
    tarif_horaire = 80
    prime = (nombre_heures_travaillees // 10) * 100
else:
    print("Grade invalide. Veuillez entrer un grade valide (A, B, C, D, ou E).")
    exit()

salaire = (tarif_horaire * nombre_heures_travaillees) + prime

print(f"Le salaire de l'employé est de {salaire} DH.")
