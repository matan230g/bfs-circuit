from sympy.logic.boolalg import Xor, And, Nand, Nor, Not, Or
from sympy import symbols, sympify, satisfiable
from sympy.logic.boolalg import to_cnf
from pysat.formula import WCNF


# key _letters_value _Integer
from interp import interp


def create_dictionary(list_statements):
    atoms
    for s in list_statements:
        atoms.append(sympify(statement).atoms())
    atoms = sympify(statement).atoms()
    map_atoms = {}
    for letter in atoms:
        if map_atoms.get(letter) is None:
            map_atoms[letter] = idx
            idx = idx + 1
    return map_atoms

def convert_statement(statement):
    statement_sympy = sympify(statement)
    statement_cnf = str(to_cnf(statement_sympy))
    statement_cnf = statement_cnf.replace('(', "")
    statement_cnf = statement_cnf.replace(')', "")
    list_statements = statement_cnf.split('&')
    literals = []
    for s in list_statements:
        literals.append(s.split('|'))
    res = [convert_letters_to_integer(x_temp) for x_temp in literals]
    return res


def convert_letters_to_integer(map_l_i, atom):
    key = atom.replace('~', '')
    int_value = map_l_i.get(key)
    if '~' in atom:
        return int_value*-1
    return int_value


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
answer = interp.convert_statement(f1)
print(to_cnf(sympify(f1)))
print(answer)

wcnf = WCNF()
# wcnf.append([1,2,3], weight=1)
# wcnf.append([4,5,6], weight=3)
# wcnf.append([4,5,6], weight=3)
