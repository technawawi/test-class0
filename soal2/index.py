# start code here
from custom_function.index import fungsiKustomku
# SOAL B3
def soal2(input):
  
  input = input if(input % 2 == 0) else input + 1
  
  for row in range(1, input):
    for col in range(1, input):
      if(row == 1 or row == 9 or col == 1 or col == 9):
        print('1', end = '')
      elif((row == 3 and (3 <= col <= 7))     or (row == 7 and (3 <= col <= 7))     or (col == 3 and (3 <= row <= 7))     or (col == 7 and (3 <= row <= 7))):
        print('3', end = '')
      elif(row == 5 and col == 5):
        print('5', end = '')
      elif((row == 2 and (2 <= col <= 8))     or (row == 8 and (2 <= col <= 8))     or (col == 2 and (2 <= row <= 8))     or (col == 8 and (2 <= row <= 8))           or (row == 4 and (4 <= col <= 7))     or (row == 6 and (4 <= col <= 6))     or (col == 4 and (4 <= row <= 6))     or (col == 6 and (4 <= row <= 6))):
        print('*', end = '')
      else:
        print(' ', end = '')
    print()