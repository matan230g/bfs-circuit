
class Gate:
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        if gate_type.find("and") != -1:
            And(gate_type, gate_name, gate_output, gate_inputs)

        if gate_type.find("inverter") != -1:
            Inverter(gate_type, gate_name, gate_output, gate_inputs)

        # self.gate_name = gate_name
        # self.gate_output = gate_output
        # self.gate_inputs = gate_inputs
        # self.gate_type = gate_type






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

        # exampel - work :)
        for node in self.gate_inputs:
            node.value = 1

        self.gate_output.value = all([i.value for i in self.gate_inputs])


class Or(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        self.gate_output.value = any([i.value for i in self.gate_inputs])

class Xor(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        xor_list = []
        for i in self.gate_inputs:
            for j in self.gate_inputs[1:]:
                xor = i.value ^ j.value
                xor_list.append(xor)
        self.gate_output.value = any([i.value for i in xor_list])

class Nor(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

class Nand(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

class Inverter(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type

        print(self.gate_type)
        print(self.gate_name)
        print(self.gate_inputs)
        print(self.gate_output)



class Buffer(Gate):
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type