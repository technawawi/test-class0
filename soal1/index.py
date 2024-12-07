# start code here
# from custom_function.index import fungsiKustomku

def crange(a, b):
    return range(a, b + 1)
def printnln(a):
    print(a, end='')

def soal1(input):
  for k in crange(1, input):
    for b in crange(1, input):
      if b == k:
        j = k * 2 - 1
        printnln(j)
      elif b == input -(k-1):
        n = b * 2 - 2
        printnln(n)
      elif b > k and b < input -(k-1):
        printnln("B")
      elif b < k and b > input -(k-1):
        printnln("A")
      else:
        printnln('_')
    print()

