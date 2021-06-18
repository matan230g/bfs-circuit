import time

import math
from pysat.examples.rc2 import RC2
from pysat.solvers import Minicard
from sympy.logic.boolalg import Xor, And, Nand, Nor, Not, Or
from sympy import symbols, sympify, satisfiable
from sympy.logic.boolalg import to_cnf
from pysat.formula import CNFPlus


class MinimalSubset_2:
    def __init__(self,k):
        self.map_atoms = {}
        self.atoms_counter = 1
        self.cnf = CNFPlus()
        self.min_card = math.inf
        self.number_of_diagnoses = 0
        self.time = 0
        self.k=k
        self.atmost_cluse=[]

    def add_soft(self, c):
        if self.map_atoms.get(c) is None:
            self.map_atoms[c] = self.atoms_counter
            self.atoms_counter += 1
        self.cnf.append([self.map_atoms[c],self.k])
    def add_atmost(self,ls):
        self.atmost_cluse=ls

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
        for k, v in self.map_atoms.items():
            if v == abs(integer):
                if integer < 0:
                    return '~' + k
                else:
                    return k

    def convert_statement(self, statement):
        statement_cnf = str(statement)
        statement_cnf = statement_cnf.replace('(', "")
        statement_cnf = statement_cnf.replace(')', "")
        list_statements = statement_cnf.split('&')
        literals_list = []
        res = []
        for s in list_statements:
            literals_list.append(s.split('|'))
        for k in literals_list:
            clu = []
            for x_temp in k:
                x_temp = x_temp.replace(" ", "")
                clu.append(self.convert_letters_to_integer(x_temp))
            res.append(clu)
            self.cnf.append(clu)
        return res
    def find_mini_card(self):
        solver = Minicard(bootstrap_with=self.cnf)
        solver.add_atmost(self.atmost_cluse, self.k)
        flag=True
        while flag:
            flag = solver.solve()
            ans = solver.get_model()
            if self.k == 0:
                self.k+=1
                self.min_card=self.k
                break
            if not flag:
                self.k+=1
                self.min_card = self.k + 1
                break
            if flag:
                self.k = self.k - 1
                solver = Minicard(bootstrap_with=self.cnf)
                solver.add_atmost(self.atmost_cluse, self.k)
    def run_solver(self):
        start_time = time.time()
        current_time=None
        self.find_mini_card()
        print('my k ',self.k)
        solver = Minicard(bootstrap_with=self.cnf)
        solver.add_atmost(self.atmost_cluse, self.k)
        while solver.solve():
            ans = solver.get_model()
            ans =[self.convert_integer_to_letters(x) for x in ans]
            print(ans)
            counter = 0
            for x in ans:
                if x.startswith('~') and 'gate' in x:
                    counter = counter + 1
                    solver.add_clause([abs(self.convert_letters_to_integer(x))])
                    print('add const',x)
            if counter==0:
                break
            self.number_of_diagnoses = self.number_of_diagnoses + 1
            current_time = time.time()
            if (current_time - start_time) / 60 >= 0.5:
                print('finish run')
        if current_time is None:
            current_time =time.time()
        self.time = current_time - start_time
