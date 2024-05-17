arg = 5

def print_params(arg):
  print(*2*(arg,), sep='\n')

for i in range(5):
  print_params(arg)
  print('')
