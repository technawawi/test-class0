# start code here
from custom_function.index import crange, printnln

def soal1 (input):
  no = 1
  for y in crange(no, input):
    for x in crange(no, input):
      odd = x * 2 - 1
      even = x * 2 - 2
      if x == y:
        printnln(odd)
      elif x == input - (y-1):
        printnln(even)
      elif x >= y and x <= input - (y-1):
        printnln("B")
      elif x <= y and x >= input - (y-1):
        printnln("A")
      else:
        printnln(" ")
    print()

soal1(9)