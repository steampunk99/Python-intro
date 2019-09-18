import random

playerHP = 5000
enemyAttackLow = 60
enemyAttackHigh = 80

while playerHP > 0:
    damage = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHP = playerHP-damage