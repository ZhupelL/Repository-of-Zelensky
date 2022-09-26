#x=int(input())
#b=int(input())
#import math
#print(pow(x, b))




a = int(input())
base = int(input())
while a > 0:
    d = a % base
    print(d, end=' ')
    a //= base
