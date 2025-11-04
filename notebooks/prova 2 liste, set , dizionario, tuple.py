#liste, set , dizionario, tuple
# Le liste sono collezioni ordinate e modificabili di elementi
# I set sono collezioni non ordinate di elementi unici
# I dizionari sono collezioni di coppie chiave-valore
# Le tuple sono collezioni ordinate e immutabili di elementi    
# Esempi di ciascuna struttura dati:

# Lista
frutti = ['mela', 'banana', 'ciliegia']
print("Lista di frutti:", frutti)       
# Aggiunta di un elemento alla lista
frutti.append('arancia')
print("Lista dopo l'aggiunta di un frutto:", frutti)
# Rimozione di un elemento dalla lista 
frutti.remove('banana')
print("Lista dopo la rimozione di un frutto:", frutti)
# Accesso a un elemento della lista
print("Primo frutto nella lista:", frutti[0])

# Set
numeri = {1, 2, 3, 4, 5}
print("\nSet di numeri:", numeri)
# Aggiunta di un elemento al set
numeri.add(6)
print("Set dopo l'aggiunta di un numero:", numeri)
# Rimozione di un elemento dal set
numeri.remove(3)
print("Set dopo la rimozione di un numero:", numeri)
# Verifica se un elemento è nel set
print("Il numero 4 è nel set?", 4 in numeri)
# Dizionario
persona = {'nome': 'Alice', 'età': 30, 'città': 'Roma'}
print("\nDizionario persona:", persona)
# Aggiunta di una coppia chiave-valore al dizionario
persona['professione'] = 'Ingegnere'
print("Dizionario dopo l'aggiunta di una professione:", persona)
# Rimozione di una coppia chiave-valore dal dizionario
del persona['età']
print("Dizionario dopo la rimozione dell'età:", persona)
# Accesso a un valore tramite la chiave
print("Nome della persona:", persona['nome'])   

# Tupla 
coordinate = (10.0, 20.0)
print("\nTupla di coordinate:", coordinate)
# Accesso a un elemento della tupla
print("Prima coordinata:", coordinate[0])
# Le tuple non possono essere modificate, quindi non possiamo aggiungere o rimuovere elementi   
# Tuttavia, possiamo creare una nuova tupla basata su quella esistente
nuove_coordinate = coordinate + (30.0,)
print("Nuova tupla di coordinate:", nuove_coordinate)

#fai esempi di ciclo con e senza indice per ogni struttura dati
# Ciclo su una lista senza indice
print("\nCiclo su una lista senza indice:")
for frutto in frutti:
    print(frutto)
# Ciclo su una lista con indice
print("\nCiclo su una lista con indice:")
for i in range(len(frutti)):
    print(f"Frutto {i}: {frutti[i]}")
# Ciclo su un set senza indice
print("\nCiclo su un set senza indice:")
for numero in numeri:
    print(numero)
# Ciclo su un dizionario senza indice
print("\nCiclo su un dizionario senza indice:")
for chiave in persona:
    print(f"{chiave}: {persona[chiave]}")
# Ciclo su un dizionario con indice (usando enumerate)
print("\nCiclo su un dizionario con indice:")
for i, chiave in enumerate(persona):
    print(f"{i}. {chiave}: {persona[chiave]}")
# Ciclo su una tupla senza indice
print("\nCiclo su una tupla senza indice:")
for coordinata in coordinate:
    print(coordinata)
# Ciclo su una tupla con indice
print("\nCiclo su una tupla con indice:")
for i in range(len(coordinate)):
    print(f"Coordinata {i}: {coordinate[i]}")   


