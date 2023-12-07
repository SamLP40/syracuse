n=input("Entrer un nombre:")

while n.isnumeric()==False:
    n=input("Erreur: saisie incorrecte. Entrer un autre nombre:")

n=int(n)
result=[n]
steps=0
# number_min=n
max_value=0
    
while n != 1:
    if n==1:
        result.append(n)
        steps=steps+1
        break
    elif n % 2==0:
        n=n//2
        steps=steps+1
        result.append(n)
        # if number_min < result[n]:
        #     number_min=result[n]
    else: 
        n= 3*n+1
        result.append(n)
        steps=steps+1
        if max_value < n:
            max_value=n

print(f"Étapes : {result}")
print(f"Hauteur : {steps}")
# print (f"Valeur passant sous le nombre d'origine: {number_min}")
print(f"Altitude maximum : {max_value}")

#A factoriser (mettre le result.append(n) et steps += 1 à la fin de la boucle)