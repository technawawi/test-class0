# start code here
from custom_function.index import crange, printnln

def soal4(input):
  for y in crange(1,input):
    for x in crange(1,input):
      if x <= y and y <= input // 2+1:
        printnln("*")
      elif x >= y and y >= input // 2+1:
        printnln("*")
      else:
        printnln(" ")
    print()        