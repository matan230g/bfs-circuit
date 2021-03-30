from gate import Gate
class Circuit:
    def __init__(self,file_path):
        self.from_file_to_circuit(file_path)

    def from_file_to_circuit(self,file_path):
        f = open(file_path, "r")
        system=f.read()
        system = system.split('.')
        self.name = system[0]
        self.outputs=system[2]
        self.inputs = system[1]
        gates = system[3].split('\n')
        self.gates = []
        for g in gates[1:]:
            self.gates.append(Gate(g))

    def print(self):
        print("name: "+self.name)
        print("outputs: "+self.outputs)
        print("inputs: "+self.inputs)
        print("gates: ")
        for g in self.gates:
            print(g)