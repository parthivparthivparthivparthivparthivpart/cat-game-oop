class Employee:
    def __init__(self, name, salary, job_title, years_of_experience):
        self.name = name
        self.salary =salary
        self.job_title = job_title
        self.years_of_experience = years_of_experience

    def calculate_salary(self):
        self.salary = self.salary * self.years_of_experience * 10000

class manager(Employee):
    def __init__(self, name, salary, job_title, years_of_experience):
        super().__init__(self, name, salary, job_title, years_of_experience)
        self.superior_permissions = True
        
    def calculate_salary(self):
        super().calculate_salary()
        self.salary += 1000
    
