# start code here
# from custom_function.index import 

def soal2(input):
    for x in range(input):
        for y in range(input):
            angka = min(x + 1, y + 1, input - x, input - y)
            if angka == 2 or (4 <= x <= 6 and 4 <= y <= 6 and (x == 4 or x == 6 or y == 4 or y == 6)):
                print('*', end='')  
            elif x == 5 and y == 5:
                print('5', end='')
            elif angka == 4:
                print(' ', end='')
            else:
                print(angka, end='')
        print()

soal2(9)
