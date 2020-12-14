from project.software.software import Software


class Hardware:

    def __init__(self, name:str, type:str, capacity:int, memory:int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        pass

    def uninstall(self, software:Software):
        pass
