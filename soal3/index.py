# start code here
from custom_function.index import crange, printnln


def soal3(input):
  for y in crange(1, input):
    for x in crange(1, input):
      if x == 5:
        g = y * 2 - 1
        printnln(g)
      elif y == 5:
        g = x * 2 - 1
        printnln(g)
      else:
        printnln(" ")
    print()        
