from z3 import *

a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')
g = Int('g')
h = Int('h')
i = Int('i')

for possible_sum in range(10,16):
    s = Solver()

    s.add(a < 10, a > 0)
    s.add(b < 10, b > 0)
    s.add(c < 10, c > 0)
    s.add(d < 10, d > 0)
    s.add(e < 10, e > 0)
    s.add(f < 10, f > 0)
    s.add(g < 10, g > 0)
    s.add(h < 10, h > 0)
    s.add(i < 10, i > 0)

    s.add(Distinct(a,b,c,d,e,f,g,h,i))
    s.add(a+b==possible_sum, b+c+d==possible_sum, d+e+f==possible_sum, f+g+h==possible_sum, h+i==possible_sum)

    x = s.check()
    if str(x) == "sat":
        m = s.model()
        vals = [m.eval(va) for va in [a,b,c,d,e,f,g,h,i]]
        print(possible_sum, vals)
