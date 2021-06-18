import time

import math
from pysat.examples.rc2 import RC2
from sympy.logic.boolalg import Xor, And, Nand, Nor, Not, Or
from sympy import symbols, sympify, satisfiable
from sympy.logic.boolalg import to_cnf
from pysat.formula import WCNF

class MinimalSubset:
    def __init__(self):
        self.map_atoms = {}
        self.atoms_counter = 1
        self.wcnf = WCNF()
        self.min_card = math.inf
        self.number_of_diagnoses=0
        self.time=0

    def add_soft(self,c):
        if self.map_atoms.get(c) is None:
            self.map_atoms[c] = self.atoms_counter
            self.atoms_counter+=1
        self.wcnf.append([self.map_atoms[c]],weight=1)
    def create_dictionary(self, statement):
        atoms = statement.atoms()
        for letter in atoms:
            if self.map_atoms.get(str(letter)) is None:
                self.map_atoms[str(letter)] = self.atoms_counter
                self.atoms_counter = self.atoms_counter + 1

    def convert_letters_to_integer(self, atom):
        key = atom.replace('~', '')
        int_value = self.map_atoms[key]
        if '~' in atom:
            return int_value * -1
        return int_value

    def convert_integer_to_letters(self, integer):
        for k,v in self.map_atoms.items():
            if v == abs(integer):
                if integer<0:
                    return '~'+k
                else:
                    return k

    def convert_statement(self, statement):
        statement_cnf = str(statement)
        statement_cnf = statement_cnf.replace('(', "")
        statement_cnf = statement_cnf.replace(')', "")
        list_statements = statement_cnf.split('&')
        literals_list = []
        res=[]
        for s in list_statements:
            literals_list.append(s.split('|'))
        for k in literals_list:
            clu=[]
            for x_temp in k:
                x_temp = x_temp.replace(" ","")
                clu.append(self.convert_letters_to_integer(x_temp))
            res.append(clu)
            self.wcnf.append(clu)
        return res

    def run_solver(self):
        start_time = time.time()
        with RC2(self.wcnf, solver='mc') as rc2:
            while True:
                ans = rc2.compute()
                if ans is None:
                    print('break no answer')
                    break
                ans = [self.convert_integer_to_letters(x) for x in ans]
                # print(ans)
                counter = 0
                for x in ans:
                    if x.startswith('~') and 'gate' in x:
                        counter = counter + 1
                        rc2.add_clause([abs(self.convert_letters_to_integer(x))])

                if counter > 0 and self.min_card > counter:
                    self.min_card = counter

                if self.min_card + 2 < counter:
                    print('break min card:',self.min_card )
                    print('number of comp: ',counter)
                    break

                self.number_of_diagnoses = self.number_of_diagnoses+1
                current_time = time.time()

                if (current_time - start_time) / 60 >= 0.5:
                    print('finish run')
                    break
            self.time = current_time-start_time