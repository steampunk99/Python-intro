import random


class Enemy:
    attackLow = 60
    attackHigh = 80

    def getAttack(self):
        print(self.attackHigh)

enemy1 = Enemy()
enemy1.getAttack()
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
