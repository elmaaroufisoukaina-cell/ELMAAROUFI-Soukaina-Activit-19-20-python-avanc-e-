adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
n=len(adresses_ip)

#La première adresse de la liste
print("La première adresse de la liste est ", adresses_ip[0])

#La dernière adresse de la liste
print("La dernière adresse de la liste est ", adresses_ip[n-1])

#La troisième adresse de la liste
print("La troisième adresse de la liste est ", adresses_ip[3-1])

#L'ajout de "172.31.0.1" à la liste
adresses_ip.append("172.31.0.1")
print(adresses_ip)

#Supprimez l'adress IP "200.100.50.1"
adresses_ip.remove("200.100.50.1")
print(adresses_ip)

#Nombres des adresses restants dans La liste 
NewNumber=len(adresses_ip)
print("Il reste",NewNumber,"adresses dans cette liste aprés les modifications")

#Verifiant si "192.168.0.1" est présente dans la liste
if "192.168.0.1" in adresses_ip:
    print("L'adresse \"192.168.0.1\" est présente dans la liste")
else:
    print("L'adresse \"192.168.0.1\" n'est pas présente dans la liste")

#La class de l'adresse IP "10.0.0.1"
def Class_ip(adresse):
    parties = adresse.split(".")
    Partie1 = int(parties[0])
    Partie2 = int(parties[1])

    
    if Partie1 == 169 and Partie2 == 254:
        return "Adresse IP de lien local (APIPA)"

    if 1 <= Partie1 <= 126:
        return "Classe A"
    elif 128 <= Partie1 <= 191:
        return "Classe B"
    elif 192 <= Partie1 <= 223:
        return "Classe C"
    return "Adresse IP publique"

print("La class de l'adresse IP \"10.0.0.1\" est ",Class_ip("10.0.0.1"))
 
#Tri des adresses IP de la liste par ordre croissant 
adresses_ip.sort()
print(adresses_ip)


#Vérifiant si toutes les adresses appartiennent à la classe C

def Classe_c(ip_liste):
    for ip in ip_liste:
        Class = Class_ip(ip)
        if "Classe C" not in Class:
            return False
    return True

if Classe_c(adresses_ip):
    print("Toutes les adresses sont de classe C")
else:
    print("Toutes les adresses ne sont pas de classe C")

#Nombres des adresses IP publique
compt = 0

for i in range(n):
    if Class_ip(adresses_ip[i]) == "Adresse IP publique":
        compt += 1

print("Il y a", compt, "adresses IP publiques dans la liste.")