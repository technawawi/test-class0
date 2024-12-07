# start code here
from custom_function.index import fungsiKustomku
# SOAL D2
def soal4(input):
  
  input = input if(input % 2 == 0) else input + 1
  
  for row in range(1, input):
    for col in range(1, input):
      if((row == col)     or (row == 5)     or (col == 1 and (0 < row < 6))   or (2 < row < 5 and col == 2)   or (row == 4 and col == 3)        or (col == 9 and (4 < row < 10))   or (5 < row < 8 and col == 8)   or (row == 6 and col == 7)):
        print('*', end = '')
      else:
        print(' ', end = '')
    print()