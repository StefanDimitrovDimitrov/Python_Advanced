from project import customer
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    d_capacity = 15
    cus_capacity = 10

    def __init__(self, name: str):
        self.name = name

        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.d_capacity

    @staticmethod
    def customer_capacity():
        return MovieWorld.cus_capacity


    def add_customer(self, customer: Customer):
        if MovieWorld.cus_capacity <= 10:
            self.customers.append(customer)
            MovieWorld.cus_capacity -= 1

    def add_dvd(self, dvd: DVD):
        if MovieWorld.d_capacity <= 15:
            self.dvds.append(dvd)
            MovieWorld.d_capacity -= 1


    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_id_list = [d for d in customer.rented_dvds if dvd_id == d.id]
        if 

    def return_dvd(self, customer_id, dvd_id):
        pass

    def __repr__(self):
        pass
