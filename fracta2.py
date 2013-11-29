import turtle

def flip_and_reverse(l):
  return list(reversed(flip(l)))


def flip(input):
  output = []
  for x in input:
    if x == 'R':
      output.append('L')
    else:
      output.append('R')
  return output

def getTurns(order):
  if order <= 1:
    return ['R']
  else:
    lower_order_turns = getTurns(order - 1)
    return lower_order_turns + ['R'] + flip_and_reverse(lower_order_turns)
  
def draw_turns(turns, step):
  for turn in turns:
    if turn == "R":
      turtle.right(90)
    else:
      turtle.left(90)
    turtle.forward(step)
    
def draw_dragon(order, step):
  draw_turns(getTurns(order), step)

if __name__ == '__main__':
  assert(flip(['R', 'R', 'R', 'R', 'L']) ==
              ['L', 'L', 'L', 'L', 'R'])
  assert(flip_and_reverse(['R', 'R', 'R', 'R', 'L']) ==
         ['R', 'L', 'L', 'L', 'L'])
  assert(getTurns(1) == ['R'])
  assert(getTurns(2) == ['R', 'R', 'L'])
  assert(getTurns(3) == ['R', 'R', 'L', 'R', 'R', 'L', 'L'])
  assert(getTurns(4) == ['R', 'R', 'L', 'R', 'R', 'L', 'L',
                         'R',
                         'R', 'R', 'L', 'L', 'R', 'L', 'L'])
