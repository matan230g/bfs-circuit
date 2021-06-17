from gate import Gate
from node import Node
from itertools import combinations
import pandas as pd
import time


class Circuit:
    def __init__(self, file_path):
        self.from_file_to_circuit(file_path)
        self.df = pd.DataFrame(columns=['System Name', 'Observation no.',
                                        'Number of Diagnoses', 'Minimal Cardinality', 'Runtime (ms)'])

    def unflipped(self):
        for g in self.gates:
            g.switch_unfilpped()

    def from_file_to_circuit(self, file_path):
        f = open(file_path, "r")
        system = f.read()
        system = system.split('.')
        self.name = system[0]
        self.inputs = self.create_node(system[1])
        self.outputs = self.create_node(system[2])
        self.nodes = self.outputs + self.inputs

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
            inputs_gate = []
            for i in temp[3:]:
                if i != "":
                    inputs_gate.append(self.find_nodes(i))
            output_node = self.find_nodes(output_gate)
            self.gates.append(Gate(gate_type, gate_name, output_node, inputs_gate))
            self.run_cnf_gates(self.gates)

    def add_observation(self, observation):
        # insert observation
        for x, input_ob in zip(observation.inputs_outputs[:len(self.inputs)], self.inputs):
            input_ob.calculate_value(x)
            observation.inputs.append(input_ob)

        for x, output_ob in zip(observation.inputs_outputs[len(self.inputs):], self.outputs):
            observation.outputs.append(Node(x))
        # for g in self.gates:
        #     g.calculate()

    def run_diagnose(self, list_gates):
        for g in list_gates:
            g.switch_flipped()
        for g in self.gates:
            g.calculate()


    def run_cnf_gates(self,list_gates):
        for gate in list_gates:
            gate.get_gate_cnf()


    def run_sat(self,observation):
        pass


    def check_fix(self, observation):
        # print(observation.number,":")
        # print ('observation outputs: ',[x.value for x in observation.outputs])
        # print('circuit outputs: ',[x.value for x in self.outputs])
        for output_observation, output_circuit in zip(observation.outputs, self.outputs):
            if output_circuit.value != output_observation.value:
                return False
        return True

    def print(self):
        # print("name: " + self.name)
        # print("outputs: " + self.outputs)
        # print("inputs: "+self.inputs)
        # print("gates: ")
        # for g in self.gates:
        #     print(g)
        pass

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
        for node in self.nodes:
            if node.name == name_node:
                return node

        new_node = Node(name_node)
        self.nodes.append(new_node)
        return new_node

    @staticmethod
    def intersection(lists_of_list, lst2):
        for ls in lists_of_list:
            if all(elem in lst2 for elem in ls):
                return True
        return False

    def create_graph_gates(self, observation):
        # Get all permutations of length 2
        # and length 2
        start_time = time.time()
        if self.check_fix(observation):
            end_time = time.time()
            new_row = {'System Name': self.name, 'Observation no.': observation.number,
                       'Number of Diagnoses': 0,
                       'Minimal Cardinality': 0, 'Runtime (ms)': round((end_time-start_time)*1000)}
            self.df = self.df.append(new_row, ignore_index=True)
            return
        visited = []

        flag = False
        for i in range(1, 40):
            comb = combinations(self.gates, i)
            if flag:
                break
            for list_of_gates in comb:
                current_time = time.time()
                if (current_time - start_time) / 60 >= 1:
                    print("observation" , observation.number)
                    # print((current_time - start_time) / 60)
                    flag = True
                    break
                if not self.intersection(visited, list_of_gates):
                    self.run_diagnose(list(list_of_gates))
                    if self.check_fix(observation):
                        # print(observation.number, ": ", [y.gate_name for y in list_of_gates])
                        # remove the visited fix gates
                        visited.append(list(list_of_gates))
                    for gate in list_of_gates:
                        gate.switch_unfilpped()

        min_cardinality = 0 if not visited else min([len(ls) for ls in visited])
        end_time = time.time()
        new_row = {'System Name': self.name, 'Observation no.': observation.number,
                   'Number of Diagnoses': len(visited),
                   'Minimal Cardinality': min_cardinality, 'Runtime (ms)': round((end_time-start_time)*1000)}
        # [self.name, observation.number, len(visited), min_cardinality]
        self.df = self.df.append(new_row,ignore_index=True)

