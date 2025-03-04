import random

class Sigma:
    def __init__(self, imie):
        self.imie = imie
        self.hp = 100
        self.atak = 10
        self.zyje = True
        self.mana = 50  
    
    def czy_zyje(self):
        if self.hp <= 0:
            self.zyje = False
        return self.zyje
    
    def damage(self, n):
        self.hp -= n
        self.czy_zyje()

    def sigma_atak(self):
        return random.randint(1, 20)  
    
    def magiczny_atak(self):
        if self.mana >= 10:
            self.mana -= 10
            return random.randint(15, 30)  
        else:
            print("Za mało many na atak magiczny!")
            return self.sigma_atak()

    def atakuje(self):
        print("1 - Podstawowy atak - A")
        print("2 - Sigma atak - B")
        print("3 - Atak magiczny - C")
        inp = input("Wybierz atak: ")
        if inp == "A" or inp == "1":
            return self.atak
        elif inp == "B" or inp == "2":
            return self.sigma_atak()
        elif inp == "C" or inp == "3":
            return self.magiczny_atak()
        else:
            print('Błędny wybór ataku, użyto podstawowego ataku')
            return self.atak

class Goblin:
    def __init__(self):
        self.hp = 40
        self.atak = 5
        self.zyje = True
        self.szybki_atak = False  
    
    def czy_zyje(self):
        if self.hp <= 0:
            self.zyje = False
        return self.zyje
    
    def damage(self, n):
        self.hp -= n
        self.czy_zyje()

    def podwojny_atak(self):
        if random.random() > 0.5:  
            self.podwojny_atak = True
            return random.randint(8, 15)
        else:
            self.podwojny_atak = False
            return self.atak

    def atakuje(self):
        if self.podwojny_atak:
            print("Goblin wykonał podwojny atak!")
            return self.podwojny_atak()
        else:
            return self.atak

print("Start gry!!!")
imie = input("Podaj imię: ")
ja_sigma = Sigma(imie)
ile = 0

while ja_sigma.czy_zyje(): 
    goblin = Goblin()
    while ja_sigma.czy_zyje() and goblin.czy_zyje():
        print(f"\nSigma ma {ja_sigma.hp} HP, Goblin ma {goblin.hp} HP.")
        print("Sigma wykonuje atak...")
        goblin.damage(ja_sigma.atakuje())  
        if goblin.czy_zyje():
            print("Goblin kontratakuje...")
            ja_sigma.damage(goblin.atakuje())  
            print(f"Po ataku Goblina, Sigma ma {ja_sigma.hp} HP.")  
        
        if not goblin.czy_zyje():
            ile += 1
            print("Zabiłem goblina!!!!")
            break  

print("aAAAAAAaaaa.....")
print("Koniec gry")
print(f"Zabiłeś {ile} goblinów")
