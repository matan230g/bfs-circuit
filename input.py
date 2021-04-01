


class Input:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.connections = []

    def add_connections_to_gate(self,gate):
        self.connections.add(gate)

    def set_value(self, value ):
        self.value = value



