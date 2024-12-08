# silahkan tambah fungsi kustom sesuai kebutuhan kalian, silahkan ganti nama function jika di butuhkan
# start code here
def crange(a, b):
  return range(1, b + 1)

def printnln(a):
  print(a, end="")

def fib(a):
  if a <= 2:
    return 1
  else:
    return fib(a-1)+fib(a-2)   