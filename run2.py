from pandas import np
from sympy import symbols

from circuit import Circuit
from minsat_2 import MinimalSubset_2
from observation import Observation

# Algorithm 2
name_file = '74283'
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

    #sum_leq
    k = c1.find_number_wrong_input(object_observation)
    solver = MinimalSubset_2(k)

    for gate in c1.gates:
        # print("before ob")
        # print(gate.cnf)
        for node in object_observation.inputs:
            # print("node:",node.name , node.value)
            gate.cnf_leq = gate.cnf_leq.subs(node.symbol,node.value)
            # print(gate.cnf)

        for node in object_observation.outputs:
            # print("node:",node.name , node.value)
            gate.cnf_leq = gate.cnf_leq.subs(node.symbol,node.value)
            # print(gate.cnf)

        # print("final cnf")
        # print(gate.cnf)
        if str(gate.cnf_leq)=='True':
            continue
        solver.create_dictionary(gate.cnf_leq)
        solver.convert_statement(gate.cnf_leq)



    gates_atmost=[-1*solver.convert_letters_to_integer(gate.gate_name) for gate in c1.gates]
    k = c1.find_number_wrong_input(object_observation)
    solver.add_atmost(gates_atmost)
        # solver.add_soft(gate.gate_name)
    print(object_observation.number)
    solver.run_solver()

    # print('Minimal Cardinality',solver.min_card)
    # print('Time:', solver.time)
    # print('Number of diagnoses',solver.number_of_diagnoses)
    k=c1.find_number_wrong_input(object_observation)
    if not np.isnan(solver.time):
        time = round(solver.time*1000)
    else:
        time = np.NaN
    new_row = {'System Name': c1.name, 'Observation no.': object_observation.number,
               'Number of Diagnoses': solver.number_of_diagnoses,
               'Minimal Cardinality': solver.min_card, 'Runtime (ms)': time}
    c1.df = c1.df.append(new_row, ignore_index=True)
c1.df.fillna("NA",inplace=True)
c1.df.to_csv(name_file+'_algo_2.csv')
    ## what output is fault
    # bad_outputs = c1.check_observation(object_observation)

    ## find the gate the fault output is belong
    # c1.find_bad_gates(bad_outputs, object_observation)
# c1.nodes[22].set_value(1)
#
# c1.print()
