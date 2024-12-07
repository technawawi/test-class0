# start code here
from custom_function.index import customRange, printNoLine

def soal4(input):
  no = 1
  center = input // 2 + 1
  for y in customRange(no, input):
    for x in customRange(no, input):
      if x <= y and y <= center:
        printNoLine("*")
      elif x >= y and y >= center:
        printNoLine("*")
      else:
        printNoLine(" ")
    print()

soal4(9)