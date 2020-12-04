class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_registration = age_restriction

        self.is_rented = False
        self.status = ''

        if self.is_rented:
            self.status = "rented"
        else:
            self.status = "not_rented"

    def __repr__(self):

        return f"{id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_registration}. Status: {self.status}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        return cls(id, name, date, age_restriction)
