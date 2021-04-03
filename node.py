class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return " node: " + self.name + " value: " + ("0" if self.value is None else str(self.value))
