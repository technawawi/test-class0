# start code here
from custom_function.index import crange, printnln

def soal1(input):
  for y in crange(1,input):
    for x in crange(1,input):
      if x == y:
        ganjil = x * 2 - 1
        printnln(ganjil)
      elif x == input - (y - 1):
        j = x * 2 - 2
        printnln(j)
      elif x > y and x < input-(y - 1):
        printnln("B")
      elif x < y and x > input - (y - 1):
        printnln("A")    
      else:
        printnln(" ")
    print()          
      
