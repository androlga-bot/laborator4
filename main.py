import lab4

player1=lab4.player('Кирсан Кайфат',200)
player2=lab4.mage('Олег',100)
print(player1.get_Name(),'мана: ',player1.get_Mana(),'жизни: ',player1.get_Life())
print(player2.get_Name(),'мана: ',player2.get_Mana(),'жизни: ',player2.get_Life())
Roshag=lab4.mob('Рошаг',190)
Kali=lab4.mob('Кали',290)
Roshag.attack(player1)
player1.heal(100)
player1.attack(Roshag,100)
print(Roshag.get_Name(),'мана: ',Roshag.get_Mana(),'жизни: ',Roshag.get_Life())
print(player1.get_Name(),'мана: ',player1.get_Mana(),'жизни: ',player1.get_Life())




