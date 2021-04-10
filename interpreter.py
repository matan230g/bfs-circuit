from circuit import Circuit
from observation import Observation

name_file = 'c17'
c1 = Circuit("Data_Systems/"+name_file+".sys")
# c1.print()

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

    c1.create_graph_gates(object_observation)

c1.df.to_csv(name_file+'.csv')
    ## what output is fault
    # bad_outputs = c1.check_observation(object_observation)

    ## find the gate the fault output is belong
    # c1.find_bad_gates(bad_outputs, object_observation)
# c1.nodes[22].set_value(1)
#
# c1.print()
