from project import customer, dvd
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:


    def __init__(self, name: str):
        self.name = name

        self.customers = []
        self.dvds = []
        self.customer_ids = {}
        self.dvd_ids = {}

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10


    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)
            self.customer_ids[customer.id] = customer


    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)
            self.dvd_ids[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.dvd_ids.get(dvd_id)
        customer = self.customer_ids.get(customer_id)

        if dvd.is_rented:
            return "DVD is already rented"

        dvd_id_list = [d for d in customer.rented_dvds if dvd_id == d.id]
        if dvd_id_list:
            return f"{customer.name} has already rented {dvd.name}"

        if customer.age <= dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id, dvd_id):
        dvd_id_list = [d for d in customer.rented_dvds if dvd_id == d.id]
        if dvd_id_list:
            customer.rented_dvds.pop()
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"
    def __repr__(self):

        customer = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))


        return '\n'.join(customer + dvds)
