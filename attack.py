import random


class Enemy:
    hp = 200

    def __init__(self, attackLow, attackHigh):
        self.attackLow = attackLow
        self.attackHigh = attackHigh

    def getAttack(self):
        print(self.attackHigh)

    def getHP(self):
        print("Enemy hp is", self.hp)


enemy1 = Enemy(65, 89)
enemy1.getAttack()
enemy1.getHP()

enemy2 = Enemy(44, 76)
enemy2.getAttack()
enemy2.getHP()
'''
playerHP = 5000
enemyAttackLow = 60
enemyAttackHigh = 80
while playerHP > 0:
    damage = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHP = playerHP-damage

    if(playerHP <= 0):
        playerHP = 0
        print("You are dead")
        break

    print("Enemy strikes for", damage, "points of damage")
    print("Current HP is ", playerHP)
'''
