class Song:

    name:str
    lenght: float
    single: bool



    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single


    def get_info(self):
        return f"{self.name} – {self.length}"
