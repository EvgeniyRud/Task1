# Create a class with a description of the worker. Any worker. employees.
# Should be @property and @name.setter + method __str__

from datetime import date

now_day_ = date.today()


class Worker:
    def __init__(self, name, year_birth, city, type):
        self._name = name
        self.__year_birth = year_birth
        self.city = city
        self.type = type

    def __str__(self):
        return f' Hello. My name is {self._name}. I am {now_day_.year - self.__year_birth} years old'

    @property
    def name(self):
        return self._name

    @property
    def year_birth(self):
        return self.__year_birth

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @year_birth.setter
    def year_birth(self, new_year_birth):
        if 1940 < new_year_birth > 2020:
            raise ValueError('Invalid year')
        self.__year_birth = new_year_birth


if __name__ == '__main__':
    john = Worker("John", 1986, "Palo-Alto", "worker")
    olga = Worker("Olga", 1988, "LA","employee")
    print(john.__str__())
    print(olga.__str__())
    # print(john.get_name())
    print(john.name)
    john.name = 'Cris'
    print(john.name)
    john.year_birth = 1995
    print(john.__str__())
