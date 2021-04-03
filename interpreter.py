from circuit import Circuit
c1 = Circuit("data/circuits/Data_Systems/74181.sys")
c1.print()

c1.nodes[22].set_value(1)

c1.print()