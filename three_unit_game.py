import random  # random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.


class Unit:
    def __init__(self, name="Warrior", hp=100, defense=10, attack=30):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        print(f"{self.name} created")

    def _unit_was_attacked(self, attack_damage=0):
        random_damage: int = round(random.random() * 10)  # random.random() - случайное число от 0 до 1.
        self.hp = self.hp + self.defense - attack_damage - random_damage
        if self.hp <= 0:
            print(f"unit {self.name} was damaged on {self.defense - attack_damage - random_damage} and was killed")
            return False
        else:
            print(f"unit {self.name} was damaged on  {self.defense - attack_damage - random_damage} hp left {self.hp}")
            return True


class Spearman(Unit):
    def __init__(self, name="Spearman", hp=100, defense=10, attack=30):
        Unit.__init__(self, name, hp, defense, attack)

    def unit_was_attacked_by(self, enemy):
        if enemy.name == "Archer":
            return self._unit_was_attacked(enemy.attack + 20)
        else:
            return self._unit_was_attacked(enemy.attack)


class Archer(Unit):
    def __init__(self, name="Archer", hp=100, defense=10, attack=30):
        Unit.__init__(self, name, hp, defense, attack)

    def unit_was_attacked_by(self, enemy):
        if enemy.name == "Horseman":
            return self._unit_was_attacked(enemy.attack + 20)
        else:
            return self._unit_was_attacked(enemy.attack)


class Horseman(Unit):
    def __init__(self, name="Horseman", hp=100, defense=10, attack=30):
        Unit.__init__(self, name, hp, defense, attack)

    def unit_was_attacked_by(self, enemy):
        if enemy.name == "Spearman":
            return self._unit_was_attacked(enemy.attack + 20)
        else:
            return self._unit_was_attacked(enemy.attack)


str_start = "For start the fight, choose a fighter '1' -> Spearman, '2' -> Archer, '3' -> Horseman: "
enter_info_done = False
choose_of_player_number: int = 1
while not enter_info_done:
    choose_of_player = input(str_start)
    if choose_of_player in ["1", "2", "3"]:
        choose_of_player_number = int(choose_of_player)
        enter_info_done = True
    else:
        print("Wrong input try again")

print("Your unit is:")
player_fighter = None
if choose_of_player_number == 1:
    player_fighter = Spearman()
elif choose_of_player_number == 2:
    player_fighter = Archer()
else:
    player_fighter = Horseman()

print("Your enemy is:")
computer_fighter = None
computer_fighter_number = random.randint(1, 3)
if computer_fighter_number == 1:
    computer_fighter = Spearman()
elif computer_fighter_number == 2:
    computer_fighter = Archer()
else:
    computer_fighter = Horseman()

first_attack = random.randint(1, 2)
if first_attack == 1:
    print("First attack is your")
else:
    print("First attack is computer")

# ---------------------------------Fight------------------------------------------------------------


continuation_of_fight = True
while continuation_of_fight:
    if first_attack == 2:
        print("Computer attack you:")
        continuation_of_fight = player_fighter.unit_was_attacked_by(computer_fighter)
        if not continuation_of_fight:
            break
        print("You attack computer:")
        continuation_of_fight = computer_fighter.unit_was_attacked_by(player_fighter)
        if not continuation_of_fight:
            break
    else:
        print("You attack computer:")
        continuation_of_fight = computer_fighter.unit_was_attacked_by(player_fighter)
        if not continuation_of_fight:
            break
        print("Computer attack you:")
        continuation_of_fight = player_fighter.unit_was_attacked_by(computer_fighter)
        if not continuation_of_fight:
            break

winner = "COMPUTER" if computer_fighter.hp > 0 else "YOU"

print("*" * 15, winner, "WON", "*" * 15)
