from circuit import Circuit
from observation import Observation
c1 = Circuit("data/circuits/Data_Systems/74181.sys")
# c1.print()

f = open('data/circuits/Data_Observations/74181_iscas85.obs', "r")
system = f.read()

observations = system.split('.')
observations.remove('')
observations_list = []

for o in observations:
    o = o.replace('(','')
    o = o.replace(')','')
    observations_list.append(Observation(o))

for object_observation in observations_list:
    c1.addObservation(object_observation)
    c1.check(object_observation)
# c1.nodes[22].set_value(1)
#
# c1.print()


