class Employees:
    raise_amount = 2000
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.current_raise_amount = Employees.raise_amount

    def add_salary(self):
        self.salary = self.salary + self.current_raise_amount

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def increase_raise_amount(cls, amount):
        cls.raise_amount = cls.raise_amount + amount

