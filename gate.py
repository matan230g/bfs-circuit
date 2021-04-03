
class Gate:
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_type = gate_type
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs

    def __str__(self):
        return "gate type: " + self.gate_type +\
               " name: " + self.gate_name +\
               " output:" + str(self.gate_output) +\
               " input:" .join(map(str,self.gate_inputs))

class And(Gate):
    def __init__(self):
        self.gate_output = all([i.value for i in self.gate_inputs])


class Or(Gate):
    def __init__(self):
        self.gate_output = any([i.value for i in self.gate_inputs])

class Xor(Gate):
    def __init__(self):
        pass
        # for i in self.gate_inputs:
        #     for j in self.gate_inputs[1:]:
        #         self.gate_output =
        # self.gate_output = [i.value for i in self.gate_inputs]

class Nor(Gate):
    pass

class Nand(Gate):
    pass

class Inverter(Gate):
    pass

class Buffer(Gate):
    pass