from sympy.logic.boolalg import Xor, And, Nand, Nor, Not, Or
from sympy import symbols, sympify, satisfiable
from sympy.logic.boolalg import to_cnf
from pysat.formula import WCNF,CNF
from pysat.examples.rc2 import RC2
from pysat.solvers import Gluecard4,Solver,Lingeling,Minicard



# key _letters_value _Integer
from interp import interp


f1 = "h1 >> ((a >> (x & Y)) & (a << (x & Y)))"
f2 = "h2 >> ((b >> (x & Y)) & (b << (z & Y)))"
f3 = "h3 >> ((w >> (a | b)) & (w << (a | b)))"


# f1_s = sympify(f1)
# f2_s = sympify(f2)
# f3_s = sympify(f3)
#
# f1_s = to_cnf(f1_s)
# f2_s = to_cnf(f2_s)
# f3_s = to_cnf(f3_s)
# dic = {}
#
# print(f3_s)
# # temp = f1_s.atoms()
# # print(f1_s.atoms())
# # print(f2_s.atoms())
# # print(f3_s.atoms())
# matan = str(f3_s)
# matan = matan.replace('(', "")
# matan = matan.replace(')', "")
# # matan=matan.replace('|',"")
# # matan=matan.replace('&',"")
# temp2 = matan.split('&')
# final = []
# for mo in temp2:
#     final.append(mo.split('|'))
#
# print(matan)
# test_list = f1_s.atoms().union(f2_s.atoms()).union(f3_s.atoms())
# i = 1
# for x in test_list:
#     if dic.get(x) is None:
#         dic[x] = i
#         i = i + 1
# for a in final:
#     for z in a:
#         if '~' in z:
#             z = z.replace('~', '')
#             temp = dic.get(z) * -1
#             mako.append(temp)
# # for k, v in dic.items():
# #     print(k, v)


interp = interp()
interp.create_dictionary(f1)
interp.create_dictionary(f2)
interp.create_dictionary(f3)
answer_1 = interp.convert_statement(f1)
answer_2 = interp.convert_statement(f2)
answer_3 = interp.convert_statement(f3)
wcnf = WCNF()
for arr in answer_1:
    wcnf.append(arr)
for arr in answer_2:
    wcnf.append(arr)
for arr in answer_3:
    wcnf.append(arr)
wcnf.append([interp.map_atoms.get('x')])
wcnf.append([interp.map_atoms.get('Y')])
wcnf.append([-1*interp.map_atoms.get('z')])
wcnf.append([-1*interp.map_atoms.get('w')])
wcnf.append([interp.map_atoms.get('h1')],weight=1)
wcnf.append([interp.map_atoms.get('h2')],weight=1)
wcnf.append([interp.map_atoms.get('h3')],weight=1)
with RC2(wcnf, solver='mc') as rc2:
    while True:
        ans = rc2.compute()
        if ans is None:
            break
        ans = [interp.convert_integer_to_letters(x) for x in ans]
        print(ans)
        for x in ans:
            if x.startswith('~') and 'h' in x:
                rc2.add_clause([abs(interp.convert_letters_to_integer(x))])
                break
    # ans_2=rc2.compute()
    # ans_2=[interp.convert_integer_to_letters(x) for x in ans_2]
    # print(ans_2)



#






