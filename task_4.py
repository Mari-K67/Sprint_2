class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if cls.hours is None:
            cls.hours = (7 - cls.rest_days) * 8
            return cls(name, hours, rest_days, email)
            
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if cls.email is None:
            cls.email = f"{cls.name}@email.com"
            return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
        
    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary