
class Gate:
    def __init__(self, gate_type, gate_name, gate_output, gate_inputs):
        self.gate_type = gate_type
        self.gate_name = gate_name
        self.gate_output = gate_output
        self.gate_inputs = gate_inputs

    # def __str__(self):
        # return "gate type: " + self.type + " name: " + self.gate_name + "output:" + self.output
