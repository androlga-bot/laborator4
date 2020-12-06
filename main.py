import lab4

def Entity(player1):
    print(player1.get_name(), '\nмана: ', player1.get_mana(), '\nжизни: ',
      player1.get_life(), '\nпозиция: ', player1.get_pos(),'\n')

    
player1=lab4.Player('Кирсан Кайфат',200)
player2=lab4.Mage('Олег',100)
Entity(player1)
Entity(player2)
Roshag=lab4.Mob('Рошаг',190)
Kali=lab4.Mob('Кали',290)
Roshag.attack(player1)
player1.heal(100)
player1.attack(Roshag,100)
Entity(Roshag)
Entity(player1)
player1.move(5)
Entity(player1)
