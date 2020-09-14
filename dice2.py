from random import choices
nrolls = 15000
ndice = 2
player1wins=0
for i in range(nrolls):
    dice = choices(range(1, 7), k=ndice)
    dice.sort(reverse=True)
    if dice[0] == dice[1]:
        continue
    dice2= choices(range(1, 7), k=3)
    dice2.sort(reverse=True)
    if dice2.count(2) >= 2:
        continue
    if dice[0] + dice[1] <= dice2[0] +dice[1]:
        player1wins +=1


print("Average roll=",player1wins/nrolls)