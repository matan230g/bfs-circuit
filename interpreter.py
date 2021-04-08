from circuit import Circuit
from observation import Observation

c1 = Circuit("data/circuits/Data_Systems/c17.sys")
# c1.print()

f = open('data/circuits/Data_Observations/c17_iscas85.obs', "r")
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

    c1.create_graph_gates(object_observation)

    ## what output is fault
    # bad_outputs = c1.check_observation(object_observation)

    ## find the gate the fault output is belong
    # c1.find_bad_gates(bad_outputs, object_observation)
# c1.nodes[22].set_value(1)
#
# c1.print()
