
from Character import Character

class Novice (Character):
    def basicAttack (self, Character):
        Character.reduceHp (self.getDamage())
        print(f" {self.getUsername()} performed Basic Attack! -{self.getDamage()}")


username = input("Your username")
character1 = Character(username)
print(character1.getHp())    




