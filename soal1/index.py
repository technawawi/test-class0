# start code here
from custom_function.index import fungsiKustomku
# SOAL A5
def soal1(input):
  
  input = input if(input % 2 == 0) else input + 1
  
  for row in range(1, input):
    for col in range(1, input):
      if(row == col):
        print(row + col - 1, end = '')
      elif(row + col == input):
        print(col * 2 - 2, end = '')
      elif(row <= col and row + col <= input):
        print('B', end = '')
      elif(row >= col and row + col >= input):
        print('A', end = '')
      else:
        print(' ', end = '')
    print()