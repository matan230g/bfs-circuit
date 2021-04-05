
class Gate:
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type
        self.flipped = False

        if gate_type.find("and") != -1:
            # And(gate_type, gate_name, gate_output, gate_inputs)
            self.gate_output.value = all([i.value for i in self.gate_inputs])

        elif gate_type.find("or") != -1:
            # Or(gate_type, gate_name, gate_output, gate_inputs)
            self.gate_output.value = any([i.value for i in self.gate_inputs])

        elif gate_type.find("xor") != -1:
            # Xor(gate_type, gate_name, gate_output, gate_inputs)
            xor_list = [i.value for i in self.gate_inputs]
            xor = xor_list.count(1)
            if xor % 2 == 0:
                self.gate_output.value = 0
            else:
                self.gate_output.value = 1

        elif gate_type.find("nor") != -1:
            # Nor(gate_type, gate_name, gate_output, gate_inputs)
            self.gate_output.value = not (any([i.value for i in self.gate_inputs]))

        elif gate_type.find("nand") != -1:
            # Nand(gate_type, gate_name, gate_output, gate_inputs)
            self.gate_output.value = not (all([i.value for i in self.gate_inputs]))

        elif gate_type.find("inverter") != -1:
            # Inverter(gate_type, gate_name, gate_output, gate_inputs)
            self.gate_output.value = not gate_inputs[0].value

        elif gate_type.find("buffer") != -1:
            # Buffer(gate_type, gate_name, gate_output, gate_inputs)
            self.gate_output.value = gate_inputs[0].value



    def __str__(self):
        return "gate type: " + self.gate_type +\
               " name: " + self.gate_name +\
               " output:" + str(self.gate_output) +\
               " input:" .join(map(str,self.gate_inputs))

class And(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):

        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = all([i.value for i in self.gate_inputs])


class Or(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = any([i.value for i in self.gate_inputs])

class Xor(Gate):
    # Any ODD Number of Inputs
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type


        xor_list = [i.value for i in self.gate_inputs]
        xor = xor_list.count(1)
        if xor % 2 == 0:
            self.gate_output.value = 0
        else:
            self.gate_output.value = 1

class Nor(Gate):
    # not or
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = not (any([i.value for i in self.gate_inputs]))


class Nand(Gate):
    # not and
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = not (all([i.value for i in self.gate_inputs]))

class Inverter(Gate):
    # not
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = not gate_output.value


class Buffer(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = gate_output.value