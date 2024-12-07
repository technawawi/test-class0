# start code here
from custom_function.index import fungsiKustomku
# SOAL E4
def soal5(input):
  
  input = input if(input % 2 == 0) else input + 1
  
  for row in range(1, input):
    for col in range(1, input):
      if((row == 1 and (0 < col < 5)) or (row == 4 and (0 < col < 5))   or (col == 1 and (0 < row < 5)) or (col == 4 and (0 < row < 5))           or (row == 1 and (5 < col < 10)) or (row == 4 and (5 < col < 10))   or (col == 6 and (0 < row < 5)) or (col == 9 and (0 < row < 5))           or (row == 6 and (0 < col < 5)) or (row == 9 and (0 < col < 5))   or (col == 1 and (5 < row < 10)) or (col == 4 and (5 < row < 10))           or (row == 6 and (5 < col < 10)) or (row == 9 and (5 < col < 10))   or (col == 6 and (5 < row < 10)) or (col == 9 and (5 < row < 10))):
        print('*', end = '')
      else:
        print(' ', end = '')
    print()