from gate import Gate
from node import Node
from itertools import combinations


class Circuit:
    def __init__(self, file_path):
        self.from_file_to_circuit(file_path)

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

    def add_observation(self, observation):
        # insert observation
        for x, input_ob in zip(observation.inputs_outputs[:len(self.inputs)], self.inputs):
            input_ob.calculate_value(x)
            observation.inputs.append(input_ob)

        for x, output_ob in zip(observation.inputs_outputs[len(self.inputs):], self.outputs):
            observation.outputs.append(Node(x))
        for g in self.gates:
            g.calculate()

    def check_observation(self, observation):

        ## observation status for compare

        observation_outputs = []
        for observation_node in observation.outputs:
            new_node_name = observation_node.name + '_observation'
            new_node = Node(new_node_name)
            new_node.set_value(observation_node.value)
            observation_outputs.append(new_node)

        for g in self.gates:
            g.calculate()
        print('except :')
        for e in self.outputs:
            print(e)
        print('observation : ')
        for o in observation_outputs:
            print(o)

        # diagnose_outputs = []
        # for (gate_out,obs_out) in zip(self.outputs,observation_outputs):
        #     obs_out_name = obs_out.name.split("_")
        #     obs_out_name = obs_out_name[0]
        #     if obs_out_name == gate_out.name and obs_out.value !=gate_out.value:
        #         diagnose_outputs.append(gate_out)
        #
        # for o in diagnose_outputs:
        #     print(o)
        #
        # return diagnose_outputs

    # def check(self, observation):
    #
    #     ## observation status for compare
    #     observation_outputs = []
    #     for observation_node in observation.outputs:
    #         new_node_name = observation_node.name + '_observation'
    #         new_node = Node(new_node_name)
    #         new_node.set_value(observation_node.value)
    #         observation_outputs.append(new_node)
    #
    #     for g in self.gates:
    #         g.calculate()
    #     print('except :')
    #     for e in self.outputs:
    #         print(e)
    #     print('observation : ')
    #     for o in observation_outputs:
    #         print(o)
    #
    #
    #     # add observation inputs to the circuit inputs
    #
    #     ## the gates create for test
    #     test_gates = []
    #     z_nodes = []
    #     # observation_inputs = []
    #     temp_list = []
    #
    #     for gate in self.gates:
    #         observation_inputs = []
    #
    #         for gate_input in gate.gate_inputs:
    #             for ob_input in observation.inputs:
    #                 if ob_input.name == gate_input.name:
    #                     observation_inputs.append(ob_input)
    #             for z_node in z_nodes:
    #                 if z_node.name == gate_input.name:
    #                     observation_inputs.append(z_node)
    #
    #         diagnose_gate = gate
    #         #
    #         if not gate.flipped:
    #             diagnose_gate = Gate(gate.gate_type,gate.gate_name,gate.gate_output,observation_inputs)
    #
    #         test_gates.append(diagnose_gate)
    #
    #         z_nodes.append(diagnose_gate.gate_output)
    #
    #     # for each gate need to get all outputs and compare with the ob
    #     compare_list_test_gates = []
    #     compare_list_observation = []
    #     diagnose_nodes = []
    #     print()
    #     print("test gates")
    #     for test_gate in test_gates:
    #         if test_gate.gate_output.name.find("o") != -1:
    #             compare_list_test_gates.append(test_gate.gate_output)
    #             print("name:" , test_gate.gate_output.name , "value" , test_gate.gate_output.value)
    #
    #     print()
    #     print("observation")
    #     for ob_output in observation_outputs:
    #         compare_list_observation.append(ob_output)
    #         print("name:" , ob_output.name , "value" , ob_output.value)
    #
    #
    #     print()
    #     for (node_test,node_observation) in zip(compare_list_test_gates,compare_list_observation):
    #         # for node_observation in compare_list_observation:
    #             node_name = node_observation.name.split("_", 1)[0]
    #         # the output is wrong
    #             if node_test.name == node_name and node_test.value != node_observation.value:
    #                 diagnose_nodes.append(node_test)
    #                 print("name:" , node_test.name , "test gate:" , node_test.value , "observation:" ,node_observation.value)
    #
    #     # print("test")
    #     return diagnose_nodes

    def find_bad_gates(self, bad_outputs, object_observation):

        # loop over every gate and flip the gate output,
        # if the problem fixed, the gate is one diagnose
        diagnosed_gates = []
        for gate in self.gates:
            # gate_flipped_output = not gate.gate_output
            print("#########################################################")
            print("New Gate")
            print(gate.gate_output.value)
            gate.gate_output.value = not gate.gate_output.value
            gate.flipped = True
            temp_bad_outputs = self.check(object_observation)

            print()
            print(gate.gate_output.value)

            if len(temp_bad_outputs) < len(bad_outputs):
                diagnosed_gates.append(gate)
                gate.gate_output.value = not gate.gate_output.value
                gate.flipped = False
                self.check(object_observation)

    def run_diagnose(self, list_gates):
        for g in list_gates:
            g.switch_flipped()
        for g in self.gates:
            g.calculate()

    def check_fix(self, observation):
        # print(observation.number,":")
        # print ('observation outputs: ',[x.value for x in observation.outputs])
        # print('circuit outputs: ',[x.value for x in self.outputs])
        for output_observation, output_circuit in zip(observation.outputs, self.outputs):
            if output_circuit.value != output_observation.value:
                return False
        print("bingo")
        return True

    def print(self):
        # print("name: " + self.name)
        # print("outputs: " + self.outputs)
        # print("inputs: "+self.inputs)
        # print("gates: ")
        for g in self.gates:
            print(g)

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

    def create_graph_gates(self, observation):
        # Get all permutations of length 2
        # and length 2
        result = []
        for i in range(1, 40):
            comb = combinations(self.gates, i)
            for x in comb:
                self.run_diagnose(list(x))
                if self.check_fix(observation):
                    print(observation.number,": ",[y.gate_name for y in x])
                for gate in x:
                    gate.switch_unfilpped()
