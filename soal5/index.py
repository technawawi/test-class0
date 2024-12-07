# start code here
from custom_function.index import crange, printnln

def soal5(input):
  for y in crange(1,input):
    for x in crange(1,input):
      if x == 4 or y == 4 or x == 1 or y == 1:
        printnln("*")
      else:
        printnln(" ")
    print()