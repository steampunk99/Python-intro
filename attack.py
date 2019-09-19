import random


class Enemy:
    def __init__(self, attackLow, attackHigh):
        self.attackLow = attackLow
        self.attackHigh = attackHigh

    def getAttack(self):
        print(self.attackHigh)

enemy1 = Enemy(65, 89)
enemy1.getAttack()

enemy2 = Enemy(44, 76)
enemy2.getAttack()
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
