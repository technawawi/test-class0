# start code here
from custom_function.index import customRange, printNoLine

def soal5(input):
  no = 1
  limiter = input // 2 + 1

  for y in customRange(no, input):
    for x in customRange(no, input):
      if x == limiter or y == limiter:
        printNoLine(" ")
      else:
        printNoLine("*")
    print()

soal5(9)
