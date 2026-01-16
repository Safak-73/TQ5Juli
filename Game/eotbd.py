# %% [markdown]
# # Rogue-Like RPG - Aktueller Projekttitel

# %%
import random


# %%
print("=========================================================")
print("Hallo und willkommen zu Eclipse of the Black Dragon! v1.0")
print("=========================================================\n")
print("In diesem Abenteuer wirst du durch Dungeons ziehen, Gegner bekämpfen und Erfahrung sammeln.")
print("Wähle deine Klasse weise und achte auf deine Werte!\n")

# %%

# Frage nachden Spielernamen
spieler_name = input("Wie lautet dein Name, Abenteurer?")
print(f"\nWillkommen, {spieler_name}! Lass uns dein Abenteuer beginnen.\n")

# %%
# Klasse
class Klasse:
    def __init__(self, name, hp, atk, defense, init):
        self.name = name # Name der Klasse
        self.hp = hp # Lebenspunkte
        self.atk = atk # Angriffswerte
        self.defense = defense # Verteidigung
        self.init = init # Initative

    def __str__(self):
        return f"{self.name} | HP: {self.hp} | ATK: {self.atk} | DEF: {self.defense} | INIT: {self.init}"

# %%
# Verfügbare Klassen
verfuegbare_klassen = [
    Klasse("Krieger", hp=150, atk=12, defense=15, init=5),
    Klasse("Schurke", hp=100, atk=18, defense=10, init=15),
    Klasse("Waldläufer", hp=70, atk=22, defense=5, init=20)
]

# %%
# Klassenwahl
def waehle_klasse(spieler_name):
    while True:
        print(f"{spieler_name}, wähle deine Klasse für dein Abenteuer:\n")

        # Zeige alle verfügbaren Klassen an
        for i, k in enumerate(verfuegbare_klassen, start=1):
            print(f"{i}. {k}")

        # Eigentliche Klassenwahl
        auswahl = input("\nDeine Wahl (1-3):")

        if auswahl in ["1", "2", "3"]:
            gewaehlte_klasse = verfuegbare_klassen[int(auswahl)-1]
            print(f"\n{spieler_name}, du hast die Klasse {gewaehlte_klasse.name} gewählt!\n")
            bestaetigung = input("Willst du diese Klasse wählen? (j/n)").lower()
            if bestaetigung == "j":
                print(f"Du bist von nun bekannt als {spieler_name} der {gewaehlte_klasse.name}!\n")
                return gewaehlte_klasse
            else:
                print("Dann wähle erneut.\n")
        else:
            print("Ungültige Wahl. Bitte wähle eine Klasse mit den Zahlen 1 bis 3.\n")

spieler_klasse = waehle_klasse(spieler_name)

# %%
#Monster Liste
monster_liste = [
    Klasse("Goblin", hp=30, atk=8, defense=3, init=10),
    Klasse("Zombie", hp=50, atk=10, defense=5, init=2),
    Klasse("Skelettkrieger", hp=40, atk=10, defense=6, init=8),
    Klasse("Naga", hp=35, atk=18, defense=4, init=12),
    Klasse("Ork", hp=80, atk=12, defense=15, init=5),
    Klasse("Dunkle Magierin", hp=25, atk=20, defense=3, init=18),
    Klasse("Schwarzer Drache", hp=200, atk=25, defense=20, init=15) # Bossgegner
]

# %%
# Die texte die der spieler bei einer Niederlage angezeigt bekommt
niederlage_texte ={
    "Goblin": "Der Goblin leert deine Tasche und erfreut sich an seinem neuen Reichtum.",
    "Zombie": "Der Zombie stürzt sich auf dich und fängt an, dich zu fressen. Wenig später steht dein toter Körper selbst auf und ist auf ewig verdammt, als Untoter durch den Dungeon zu streifen.",
    "Skelettkrieger": "Als der Skelettkrieger dich trifft, spürst du, wie das Leben deinem Körper entweicht. Jahre später, nachdem dein Fleisch verwest ist, regt sich dein Gerippe, um dem Schwarzen Drachen in seiner Armee der Untoten zu dienen.",
    "Naga": "Die Naga ringt dich nieder. Als du dachtest, sie wird dich töten, umwickelt dich die Naga mit ihrem Schlangenkörper und schleift dich davon. Schnell stellst du fest, sie wird dich nicht töten, sondern viel Schlimmeres... dich heiraten. Fünf Jahre später bist du gefangen in einer unglücklichen Ehe, musst dich um die vielen kleinen Nagakinder kümmern, während sie weiterhin in der Armee des Schwarzen Drachen dient.",
    "Ork": "Als du zu Boden gehst, schaust du erschöpft zu dem Ork hoch. Er packt dich an den Haaren und schleift dich zu dem Lager der Orks. Hier musst du nun bis zum Ende deiner Tage als Sklave dienen.",
    "Dunkler Magier": "Als du zu Boden gehst, tötet dich der dunkle Magier nicht. Er verwandelt dich stattdessen in eine schwarze Katze, und du musst dein restliches Leben als Haustier fristen.",
    "Schwarzer Drache": "Du warst dem Ziel so nahe, doch der schwarze Drache ist einfach zu mächtig. Er hat dich besiegt, tötet dich aber nicht. Er lässt dich gefangen nehmen und geht zu deinem Haus. Er macht deiner Mutter den Hof und heiratet sie. Der Drache hat somit deine Mutter gefickt."
}

# %%
# Kampfsystem
def kampf(spieler, monster):
    print(f"\nEin wildes {monster.name} taucht auf")

    if spieler.init >= monster.init:
        angreifer, verteidiger = spieler, monster
    else:
        angreifer, verteidiger = monster, spieler

    while spieler.hp > 0 and monster.hp > 0:
        schaden = max(1, angreifer.atk - verteidiger.defense)
        verteidiger.hp -= schaden
       
        if angreifer == monster:
            print(f"{monster.name} greift dich an! Du hast noch {spieler.hp} HP übrig")
        
        elif angreifer == spieler:
            print(f"Du greifst {monster.name} an und triffst es!")
        
        if verteidiger.hp <= 0:
            if verteidiger == monster:
                print(f"Du hast {monster.name} besiegt!")
            else:
                print(niederlage_texte.get(monster.name, "Du wurdest besiegt!"))
            break
    
        angreifer, verteidiger = verteidiger, angreifer

    return spieler.hp > 0


# %%
#game start abfrage
def game_start(spieler_name, spieler_klasse):
    while True:
        print("\nMöchtest du den dunklen Dungeon betreten und dein Abenteuer beginnen?")

        if input("Gib 'j' ein, um zu starten: ").lower() == 'j':
            print("\nDu gehst du dunklen Stufen in die Schwärze hinab. Nur der Schein deiner Fackel erhellt den Weg vor dir.")
            return True
        else:
            print("Du beschließt, doch lieber zum dorf zurückzukehren. Statt ein strahlender Held zu werden, führst du ein langweiliges Leben, aber langes leben als Bauer.")
            input()

game_start(spieler_name, spieler_klasse)

# %%
# Random encounter
def zufallsbegegnung(spieler):
    boss_wahrscheinlichkeit = 0.1

    if random.random() < boss_wahrscheinlichkeit:
        monster = next(m for m in monster_liste if m.name == "Schwarzer Drache")
    else:
        monster = random.choice([m for m in monster_liste if m.name != "Schwarzer Drache"])
    spieler_lebt = kampf(spieler, monster)
    return spieler_lebt
    


# %%
# Spiel start
if game_start(spieler_name, spieler_klasse):
    while True:
        input("\nDrücke Enter, um weiterzugehen...")
        lebt = zufallsbegegnung(spieler_klasse)
        if not lebt:
            print("\nDas Abenteuer endet hier. Game over")
            break


