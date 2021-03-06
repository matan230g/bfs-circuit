import re
from sympy.logic.boolalg import Xor, And, Nand, Nor, Not, Or, Equivalent, Implies, to_cnf
from sympy import symbols, sympify


class Gate:
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type
        self.flipped = False
        self.symbol = symbols(self.gate_name)
        self.cnf = ""
        self.cnf_leq = ""


    def get_gate_cnf_leq(self):
        gate_logic = None

        input_0 = self.gate_inputs[0].symbol
        if len(self.gate_inputs) > 1:
            input_1 = self.gate_inputs[1].symbol

        output = self.gate_output.symbol

        if re.match("^and", self.gate_type):
            gate_logic = And(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = And(gate_logic, self.gate_inputs[idx].symbol)

            # gate_logic = Xor(gate_logic,Not(self.gate_name))


        elif re.match("^or", self.gate_type):
            gate_logic = Or(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = Or(gate_logic, self.gate_inputs[idx].symbol)

            # gate_logic = Xor(gate_logic,self.gate_name)

        elif re.match("^xor", self.gate_type):
            gate_logic = Xor(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = Xor(gate_logic, self.gate_inputs[idx].symbol)

            # gate_logic = Xor(gate_logic,self.gate_name)

        elif re.match("^nor", self.gate_type):
            gate_logic = Or(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = Or(gate_logic, self.gate_inputs[idx].symbol)
            gate_logic = Not(gate_logic)

            # gate_logic = Xor(gate_logic,self.gate_name)

        elif re.match("^nand", self.gate_type):
            gate_logic = And(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = And(gate_logic, self.gate_inputs[idx].symbol)
            gate_logic = Not(gate_logic)

            # gate_logic = Xor(gate_logic,self.gate_name)

        elif self.gate_type.find("inverter") != -1:
            gate_logic = Not(input_0)

            # gate_logic = Xor(gate_logic,self.gate_name)

        elif self.gate_type.find("buffer") != -1:
            gate_logic = Not(Not(input_0))

            # gate_logic = Xor(gate_logic,self.gate_name)

        gate_logic = Xor(gate_logic, Not(self.gate_name))
        self.cnf_leq = Equivalent(output, gate_logic)
        # print(self.cnf)
        self.cnf_leq = to_cnf(self.cnf_leq)
        # print(to_cnf(self.cnf))

    def get_gate_cnf(self):
        gate_logic = None
        input_0 = self.gate_inputs[0].symbol
        if len(self.gate_inputs) > 1:
            input_1 = self.gate_inputs[1].symbol

        output = self.gate_output.symbol

        if re.match("^and", self.gate_type):
            gate_logic = And(input_0, input_1)
            if len(self.gate_inputs)>2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = And(gate_logic, self.gate_inputs[idx].symbol)

        elif re.match("^or", self.gate_type):
            gate_logic = Or(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = Or(gate_logic, self.gate_inputs[idx].symbol)

        elif re.match("^xor", self.gate_type):
            gate_logic = Xor(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = Xor(gate_logic, self.gate_inputs[idx].symbol)

        elif re.match("^nor", self.gate_type):
            gate_logic = Or(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = Or(gate_logic, self.gate_inputs[idx].symbol)
            gate_logic = Not(gate_logic)

        elif re.match("^nand", self.gate_type):
            gate_logic = And(input_0, input_1)
            if len(self.gate_inputs) > 2:
                for idx in range(2, len(self.gate_inputs)):
                    gate_logic = And(gate_logic, self.gate_inputs[idx].symbol)
            gate_logic = Not(gate_logic)

        elif self.gate_type.find("inverter") != -1:
            gate_logic = Not(input_0)

        elif self.gate_type.find("buffer") != -1:
            gate_logic = Not(Not(input_0))


        self.cnf = Implies(self.symbol,Equivalent(output,gate_logic))
        # print(self.cnf)
        self.cnf = to_cnf(self.cnf)
        # print(to_cnf(self.cnf))






    def switch_flipped(self):
        if not self.flipped:
            self.flipped = True
            self.gate_output.value = not self.gate_output.value

    def switch_unfilpped(self):
        if self.flipped:
            self.flipped = False
            self.gate_output.value = not self.gate_output.value

    def calculate(self):
        if re.match("^and", self.gate_type):
            self.gate_output.value = all([i.value for i in self.gate_inputs])

        elif re.match("^or", self.gate_type):
            self.gate_output.value = any([i.value for i in self.gate_inputs])

        elif re.match("^xor", self.gate_type):
            xor_list = [i.value for i in self.gate_inputs]
            xor = xor_list.count(1)
            if xor % 2 == 0:
                self.gate_output.value = False
            else:
                self.gate_output.value = True

        elif re.match("^nor", self.gate_type):

            self.gate_output.value = not (any([i.value for i in self.gate_inputs]))

        elif re.match("^nand", self.gate_type):

            self.gate_output.value = not (all([i.value for i in self.gate_inputs]))

        elif self.gate_type.find("inverter") != -1:

            self.gate_output.value = not self.gate_inputs[0].value

        elif self.gate_type.find("buffer") != -1:
            self.gate_output.value = self.gate_inputs[0].value
        if self.flipped:
            self.gate_output.value = not self.gate_output.value

    def __str__(self):
        return "gate type: " + self.gate_type + \
               " name: " + self.gate_name + \
               " output:" + str(self.gate_output) + \
               " input:".join(map(str, self.gate_inputs))
