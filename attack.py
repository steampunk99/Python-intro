import random

playerHP = 5000
enemyAttackLow = 60
enemyAttackHigh = 80

while playerHP > 0:
    damage = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHP = playerHP-damage

    if(playerHP <= 0):
        playerHP = 0
        print("You are dead")
