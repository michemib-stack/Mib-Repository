class Studente:
  def __init__(self, nome, cognome, corso_di_studi, listavoti):  #metodo init, iniziale
    self.nome = nome
    self.cognome = cognome
    self.corso_di_studi = corso_di_studi
    self.listavoti = listavoti

  def Dati(self):                             # metodi creati da me
    return 'Nome:' + self.nome + '\n' + \
           'Cognome:' + self.cognome + '\n' + \
           'Corso di studi:' + self.corso_di_studi + '\n' + \
           'lista voti:' + str(self.listavoti)

  def Media(self):
    #return 'Media voti: ' + str(sum(self.listavoti)/len(self.listavoti))
    return sum(self.listavoti)/len(self.listavoti)

studente1 = Studente('Mario', 'Rossi','Ingegneria',[30,18,23])
studente2 = Studente('Pippo', 'Baudo','ScienzePol',[19,18,21])

print(studente1)
print(studente2)



#del studente1.nome


print()
print(studente1.Dati())

studente1.corso_di_studi = 'Matematica'  # aggiorno istanza
print('ristampo dopo aver cambiato corso')
print(studente1.Dati())

print(studente1.Media())
print()
print(studente2.Dati())
print(studente2.Media())

print(type(studente1))
print(type(studente1.Media()))

print(Studente.Dati(studente1))
f"Media voti: {studente1.Media()}"

class Tutore(Studente):   # definisco una classe Tutore  che eredita struttura e attributi della classe studente
  pass

  def Livello(self):                             # metodi creati da me
      return 'Turore in materie di :' + self.corso_di_studi + '\n'


tutore1 = Tutore('Gino', 'Vanelli','Teologia',[20,18,23])

print(tutore1.Livello())

#print(studente1.Livello())

# definisci una classe militare che eredida da studente, e in piu ha gli attributi di giorni di permesso, che calcola i gg di permesso
# in base alla media se sueriore a 20 allora 2 g se minore 1g se maggiore di 30 allora 3g


class Militare(Studente):
    pass
    #def __init__(self, nome, cognome, corso_di_studi, listavoti): #qui posso aggiungere altri attributi
    #   super().__init__(nome, cognome, corso_di_studi, listavoti) # richiamo il costruttore della classe base
  

    def GiorniPermesso(self):
        #media = sum(self.listavoti) / len(self.listavoti)
        media = self.Media() # Corrected to call the instance method Media()
        if media > 30:
            return 3
        elif media > 20:
            return 2
        else:
            return 1

militare1 = Militare('Luca', 'Verdi', 'Fanfara', [25, 28, 26])
print(f"{militare1.Dati()}")
print(f"Giorni di permesso: {militare1.GiorniPermesso()}")

militare2 = Militare('Anna', 'Neri', 'Logistica', [18, 20, 19])
print(f"\n{militare2.Dati()}")
print(f"Giorni di permesso: {militare2.GiorniPermesso()}")

militare3 = Militare('Paolo', 'Bianchi', 'Comunicazioni', [30, 30, 30])
print(f"\n{militare3.Dati()}")
print(f"Giorni di permesso: {militare3.GiorniPermesso()}")

import prova22

import math
print("\nValore di pi greco:", math.pi) 
print("Radice quadrata di 16:", math.sqrt(16))

max_val = max(10, 20, 5, 30)
min_val = min(10, 20, 5, 30)
print("Valore massimo:", max_val)
print("Valore minimo:", min_val)  



import datetime as dt

x = dt.datetime.now()
print("Data e ora attuali:", x)
print(x.strftime("%b")) # Month as locale’s abbreviated name.
print(x.strftime("%A")) # Weekday as locale’s full name.  
print(x.strftime("%d")) # Day of the month as a zero-padded decimal number.
print(x.strftime("%Y")) # Year with century as a decimal number.
print(x.strftime("%H:%M:%S")) # Hour, Minute and Second
print(x.strftime("%I:%M %p")) # Hour and Minute, 12-hour clock, AM or PM
print(x.strftime("%c")) # Locale’s appropriate date and time representation.
print(x.strftime("%x")) # Locale’s appropriate date representation.
print(x.strftime("%X")) # Locale’s appropriate time representation.
#parametro per il formato Giuliano?
print(x.strftime("%j")) # Day of the year as a zero-padded decimal number.

