import time


class Hero:

    def __init__(self, name, strength, speed):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.life = 100
        print("-----------------------")
        print(f"Создан герой '{name}'")
        print(f"Сила: {strength}/100")
        print(f"Скорость: {speed}/100")

    def attack(self):
        return self.strength + (self.strength*(self.speed//100))//100
        # attack = (strength + (streght*(speed/100)))/100

    def defend(self):
        return 4


def fighting(hero1, hero2):
    while (hero1.life > 0) and (hero2.life > 0):
        hero2.life = hero2.life - hero1.attack()
        print(f"{hero1.name} атакует {hero2.name}")
        print(f"Здоровье {hero2.name} := {hero2.life}")
        hero1.life = hero1.life - hero2.attack()
        print()
        print(f"{hero2.name} атакует {hero1.name}")
        print(f"Здоровье {hero1.name} := {hero1.life}")
        print("------------------------------")
        time.sleep(0.5)

    if hero1.life < 0 and hero2.life < 0:
        print("Ничья")
    elif hero2.life > 0:
        print(f"{hero2.name} победил!")
    else:
        print(f"{hero1.name} победил!")



leo = Hero("Леонардо", 60, 60)
raf = Hero("Раф", 65, 52)
fighting(leo, raf)


