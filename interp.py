
from sympy.logic.boolalg import Xor, And, Nand, Nor, Not, Or
from sympy import symbols, sympify, satisfiable
from sympy.logic.boolalg import to_cnf
from pysat.formula import WCNF

class interp:
    def __init__(self):
        self.map_atoms = {}
        self.atoms_counter = 1

    def create_dictionary(self, statement):
        atoms = sympify(statement).atoms()
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

    def convert_statement(self, statement):
        statement_sympy = sympify(statement)
        statement_cnf = str(to_cnf(statement_sympy))
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
        return res
