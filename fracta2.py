import turtle

def flip_and_reverse(l):
  if l == ['R']:
    return ['L']
  elif l == ['R', 'R', 'L']:
    return ['R', 'L', 'L']
  else:
    raise ValueError("I DON'T KNOW THE ANSWER!!!1!")

def getTurns(order):
  if order <= 1:
    return ['R']
  else:
    lower_order_turns = getTurns(order - 1)
    return lower_order_turns + ['R'] + flip_and_reverse(lower_order_turns)

assert(getTurns(1) == ['R'])
assert(getTurns(2) == ['R', 'R', 'L'])
assert(getTurns(3) == ['R', 'R', 'L', 'R', 'R', 'L', 'L'])
assert(getTurns(4) == ['R', 'R', 'L', 'R', 'R', 'L', 'L',
                       'R'
                       'R', 'R', 'L', 'L', 'R', 'L', 'L'])