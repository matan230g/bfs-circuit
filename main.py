from sympy.logic.boolalg import Xor,And,Nand,Nor,Not,Or
from sympy import symbols, sympify, satisfiable
from sympy.logic.boolalg import to_cnf
from pysat.formula import WCNF

f1 = "h1 >> ((a >> (x & Y)) & (a << (x & Y)))"
f2 = "h2 >> ((b >> (x & Y)) & (b << (z & Y)))"
f3 = "h3 >> ((w >> (a | b)) & (w << (a | b)))"
f1_s = sympify(f1)
f2_s =sympify(f2)
f3_s=sympify(f3)

f1_s = to_cnf(f1_s)
f2_s =to_cnf(f2_s)
f3_s=to_cnf(f3_s)
dic =  {}

print(f3_s)
# temp = f1_s.atoms()
# print(f1_s.atoms())
# print(f2_s.atoms())
# print(f3_s.atoms())
matan = str(f3_s)
matan=matan.replace('(',"")
matan=matan.replace(')',"")
# matan=matan.replace('|',"")
# matan=matan.replace('&',"")
temp2 = matan.split('&')
final=[]
for mo in temp2:
    final.append(mo.split('|'))

print(matan)
test_list = f1_s.atoms().union(f2_s.atoms()).union(f3_s.atoms())
i=1
for x in test_list:
    if dic.get(x) is None:
        dic[x]=i
        i = i + 1
for a in final:
    for z in a:
        if '~' in z:
            z= z.replace('~','')
            temp =dic.get(z)*-1
            mako.append(temp)
# for k, v in dic.items():
#     print(k, v)
wcnf = WCNF()
# wcnf.append([,2,3], weight=1)
# wcnf.append([4,5,6], weight=3)
# wcnf.append([4,5,6], weight=3)