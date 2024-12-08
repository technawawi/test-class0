# start code here
from custom_function.index import crange, printnln

def soal2(input):
  for y in crange(-4, 4):
    for x in crange(-4, 4):
      n = abs(x) if abs(x) > abs(y) else abs(y)
      n = 4 - n + 1
      if n % 2 == 0:
        printnln(" ")
      else:
        printnln(n)
    
    print()  
 