from gate import Gate
from node import Node


class Circuit:
    def __init__(self, file_path):
        self.from_file_to_circuit(file_path)

    def from_file_to_circuit(self, file_path):
        f = open(file_path, "r")
        system = f.read()
        system = system.split('.')
        self.name = system[0]
        self.inputs = self.create_node(system[1])
        self.outputs = self.create_node(system[2])
        self.nodes = self.outputs

        gates = system[3].split('\n')
        gates.remove('')

        self.gates = []
        for g in gates:
            txt = g.replace('[', '')
            txt = txt.replace(']', '')
            temp = txt.split(',')
            gate_type = temp[0]
            gate_name = temp[1]
            output_gate = temp[2]
            inputs_gate =[]
            for i in temp[3:]:
                if i != "":
                    inputs_gate.append(Node(i))
            output_node = self.find_nodes(output_gate)
            self.gates.append(Gate(gate_type,gate_name,output_node,inputs_gate))


    def print(self):
        print("name: " + self.name)
        # print("outputs: " + self.outputs)
        # print("inputs: "+self.inputs)
        # print("gates: ")
        # for g in self.gates:
        #     print(g)

    @staticmethod
    def create_node(nodes):
        nodes = nodes.replace('[', '')
        nodes = nodes.replace('\n', '')
        nodes = nodes.replace(']', '')
        nodes = nodes.split(',')
        list_nodes = []
        for n in nodes:
            list_nodes.append(Node(n))
        return list_nodes

    def find_nodes(self, name_node):
        if name_node in [lambda x: x.name in self.nodes]:
                return x
            else:
                new_node = Node(name_node)
                self.nodes.append(new_node)
                return new_node

