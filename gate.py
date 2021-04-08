import re


class Gate:
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs
        self.gate_type = gate_type
        self.flipped = False

    def switch_flipped(self):
        if not self.flipped:
            self.flipped = True
            self.gate_output.value = not self.gate_output.value

    def switch_unfilpped(self):
        if self.flipped:
            self.flipped = False
            self.gate_output.value = not self.gate_output.value

    def calculate(self):
        if not self.flipped:

            if re.match("^and", self.gate_type):
                # And(gate_type, gate_name, gate_output, gate_inputs)
                self.gate_output.value = all([i.value for i in self.gate_inputs])


            elif re.match("^or", self.gate_type):
                # Or(gate_type, gate_name, gate_output, gate_inputs)
                self.gate_output.value = any([i.value for i in self.gate_inputs])

            elif re.match("^xor", self.gate_type):
                xor_list = [i.value for i in self.gate_inputs]
                xor = xor_list.count(1)
                if xor % 2 == 0:
                    self.gate_output.value = False
                else:
                    self.gate_output.value = True

            elif re.match("^nor", self.gate_type):
                # Nor(gate_type, gate_name, gate_output, gate_inputs)
                self.gate_output.value = not (any([i.value for i in self.gate_inputs]))

            elif re.match("^nand", self.gate_type):
                # Nand(gate_type, gate_name, gate_output, gate_inputs)

                self.gate_output.value = not (all([i.value for i in self.gate_inputs]))

            elif self.gate_type.find("inverter") != -1:
                # Inverter(gate_type, gate_name, gate_output, gate_inputs)
                self.gate_output.value = not self.gate_inputs[0].value

            elif self.gate_type.find("buffer") != -1:

                # Buffer(gate_type, gate_name, gate_output, gate_inputs)
                self.gate_output.value = self.gate_inputs[0].value

    def __str__(self):
        return "gate type: " + self.gate_type + \
               " name: " + self.gate_name + \
               " output:" + str(self.gate_output) + \
               " input:".join(map(str, self.gate_inputs))

# class And(Gate):
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#         self.gate_output.value = all([i.value for i in self.gate_inputs])
#
#
#
#
# class Or(Gate):
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#
#         self.gate_output.value = any([i.value for i in self.gate_inputs])
#
# class Xor(Gate):
#     # Any ODD Number of Inputs
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#
#
#         xor_list = [i.value for i in self.gate_inputs]
#         xor = xor_list.count(1)
#         if xor % 2 == 0:
#             self.gate_output.value = 0
#         else:
#             self.gate_output.value = 1
#
# class Nor(Gate):
#     # not or
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#
#         self.gate_output.value = not (any([i.value for i in self.gate_inputs]))
#
#
# class Nand(Gate):
#     # not and
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#
#         self.gate_output.value = not (all([i.value for i in self.gate_inputs]))
#
# class Inverter(Gate):
#     # not
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#
#         self.gate_output.value = not gate_output.value
#
#
# class Buffer(Gate):
#     def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
#         self.gate_name = gate_name
#         self.gate_output = gate_output
#         self.gate_inputs = gate_inputs
#         self.gate_type = gate_type
#
#         self.gate_output.value = gate_output.value
