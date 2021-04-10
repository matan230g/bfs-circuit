from circuit import Circuit
from observation import Observation

name_file = 'c17'

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

    c1.create_graph_gates(object_observation)

c1.df.to_csv(name_file+'.csv')



