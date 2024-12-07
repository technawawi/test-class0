# start code here
from custom_function.index import fungsiKustomku
# SOAL C5
def soal3(input):
  
  input = input if(input % 2 == 0) else input + 1
  
  for row in range(1, input):
    for col in range(1, input):
      if(row == 5 and col == 5):
        print('9', end = '')
      elif((row == 4 and col == 5)    or (row == 5 and col == 6)    or (row == 6 and col == 5)    or (row == 5 and col == 4)):
        print('7', end = '')
      elif((col - row == 2 and (8 <= row + col <= 12))    or (row + col == 12 and (col - row <= 3 and row - col <= 3))    or (row - col == 2 and (5 <= row <= 7))    or (row + col == 8 and (3 <= row <= 5))):
        print('5', end = '')
      elif((col - row == 3 and (row != 1 and col != 4) and (row != 6 and col != 9))   or (row + col == 13 and (col != 9 and row != 4) and (row != 9 and col != 4))    or (row - col == 3 and (row != 9 and col != 6) and (row != 4 and col != 1))   or (row + col == 7 and (row != 6 and col != 1) and (row != 1 and col != 6))):
        print('3', end = '')
      elif((col - row == 4)   or (row + col == 14)    or (row - col == 4)   or (row + col == 6)):
        print('1', end = '')
      else:
        print(' ', end = '')
    print()