moves = ['paper', 'rock', 'scissor']
player_move = ''

while player_move not in moves :
  player_move = input('Choose paper, rock, scissor: ').lower()

bot_move = 'rock'
if (player_move == 'paper') :
  bot_move = 'scissor'
elif (player_move == 'rock') :
  bot_move = 'paper'

print('\nbot has choosen:', bot_move)
print('You Lose! Try Again!')
