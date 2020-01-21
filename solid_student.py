class Student():

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old and is in cohort {self.cohort}."

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0
    
    @first_name.setter
    def first_name(self, new_fname):
        if type(new_fname) is str:
            self.__first_name = new_fname
        else:
            raise TypeError('Please input a string value for the first name.')


    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0
    
    @last_name.setter
    def last_name(self, new_lname):
        if type(new_lname) is str:
            self.__last_name = new_lname
        else:
            raise TypeError('Please input a string value for the last name.')


    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    
    @age.setter 
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError('Please input an integer value for age')

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0
    
    @cohort.setter 
    def cohort(self, cohort):
        if type(cohort) is int:
            self.__cohort = cohort
        else:
            raise TypeError('Please input an integer value for cohort')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



adam = Student()

adam.first_name = "Adam"
adam.last_name = "Byrd"
adam.age = 26
adam.cohort = 36
print(adam.full_name)

print(adam)
