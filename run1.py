from sympy import symbols

from circuit import Circuit
from minimalsubset import MinimalSubset
from observation import Observation

# Algorithm 1

name_file = 'c499'
c1 = Circuit("Data_Systems/"+name_file+".sys")


f = open('Data_Observations/'+name_file+'_iscas85.obs', "r")
system = f.read()

observations = system.split('.')
observations.remove('')
observations_list = []

for o in observations:
    o = o.replace('(', '')
    o = o.replace(')', '')
    observations_list.append(Observation(o))



for object_observation in observations_list:
    c1.add_observation(object_observation)
    # print('inputs:')
    # for i in object_observation.inputs:
    #     print(i.value,end='')
    # print()
    # print('outputs:')
    # for o in object_observation.outputs:
    #     print(o.value,end=',')
    # print()
    solver = MinimalSubset()
    for gate in c1.gates:
        # print("before ob")
        # print(gate.cnf)
        for node in object_observation.inputs:
            # print("node:",node.name , node.value)
            gate.cnf = gate.cnf.subs(node.symbol,node.value)
            # print(gate.cnf)

        for node in object_observation.outputs:
            # print("node:",node.name , node.value)
            gate.cnf = gate.cnf.subs(node.symbol,node.value)
            # print(gate.cnf)

        # print("final cnf")
        # print(gate.cnf)
        if str(gate.cnf)=='True':
            continue
        solver.create_dictionary(gate.cnf)
        solver.convert_statement(gate.cnf)


    for gate in c1.gates:
        solver.add_soft(gate.gate_name)
    solver.run_solver()
    # print('Minimal Cardinality',solver.min_card)
    # print('Time:', solver.time)
    # print('Number of diagnoses',solver.number_of_diagnoses)
    new_row = {'System Name': c1.name, 'Observation no.': object_observation.number,
               'Number of Diagnoses': solver.number_of_diagnoses,
               'Minimal Cardinality': solver.min_card, 'Runtime (ms)': round(solver.time * 1000)}
    c1.df = c1.df.append(new_row, ignore_index=True)

c1.df.to_csv(name_file+'.csv')
    ## what output is fault
    # bad_outputs = c1.check_observation(object_observation)

    ## find the gate the fault output is belong
    # c1.find_bad_gates(bad_outputs, object_observation)
# c1.nodes[22].set_value(1)
#
# c1.print()
