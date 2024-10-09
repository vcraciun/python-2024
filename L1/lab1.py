import time
import os
import sys
import random

def myf(*args):
    for i in range(len(args)):
        print(args[i])

def myf2(**args):
    #for el in args.items:
    for i, (k,v) in enumerate(args.items()):
        print(k,v)

def suma(a,b):
    if type(a) is str and (type(b) is int or type(b) is float):
        return a+str(b)
    elif type(b) is str and (type(a) is int or type(a) is float):
        return str(a)+b
    else:
        return a+b
          
def use_global():
    print(var1)

var1 = "Welcome to Python"       

def main():      

    x=suma(4,5)
    y=suma("abc", "xyz")
    z=suma(1.5, 4.5)
    p=suma("abc", 123)
    q=suma(123, "abc")

    print(x, y, z, p, q)

    for i in range(10):
        print(i, end=" ")
    print()
    j = 1
    s = 0
    while j <= 100:
        s += j
        j += 1
    print(s)

    for i in range(3):
        print(f"{hex(i)[2:]:<4}", end= " ")
    print()

    s = "Hello World"
    c = s[-5:]
    print(c)

    use_global()

    myf(1,7,21,4.5,"abc","hello")
    myf2(var1="abc", v4=15,a9=5.5,t3="hello")

    r = random.choice(range(100))
    print(r)

    #1-100 
    #v = input("dati numarul: ")
    #print(v)

#ghiceste numarul 1-100
#dist(random, input) < 10  --> fierbinte
#dist(random, input) < 50  --> cald
#dist(random, input) >= 50 --> rece
#dist(random, input) == 0  --> ai ghicit

if __name__ == "__main__":
    main()