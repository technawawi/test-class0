# start code here
from custom_function.index import customRange, printNoLine

def soal1(input):
  no = 1
  for y in customRange(no, input):
    for x in customRange(no, input):
      odd = x * 2 - 1
      even = x * 2 - 2
      if x == y:
        printNoLine(odd)
      elif x == input - (y-no):
        printNoLine(even)
      elif x >= y and x <= input - (y-no):
        printNoLine("B")
      elif x <= y and x >= input - (y-no):
        printNoLine("A")
      else:
        printNoLine(" ")
    print()
      
soal1(10)